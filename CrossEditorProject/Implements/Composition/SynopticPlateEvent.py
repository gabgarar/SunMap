import squircle
from numba import jit

from Implements.Event import Event
import numpy as np
from reproject import reproject_interp

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS

import sunpy.map
import sunpy.sun







def getDegreesFromNDays(numDays, width):
    T = 25.4
    deg = numDays * 360 / T
    numPixInImage = deg * width / 180
    return numPixInImage


class SynopticPlateEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Plate Carrée : Apply the transformation to the image."

    def equ(self, elem, comm):

        shape_out = [720, 1440]
        frame_out = SkyCoord(0, 0, unit=u.deg,
                             frame="heliographic_stonyhurst",
                             obstime=elem.date)
        header = sunpy.map.make_fitswcs_header(shape_out,
                                               frame_out,
                                               scale=[180 / shape_out[0],
                                                      360 / shape_out[1]] * u.deg / u.pix,
                                               projection_code="CAR")
        out_wcs = WCS(header)

        array, footprint = reproject_interp(elem, out_wcs, shape_out=shape_out)

        return array

    def getElapsedTime(self, maps):
        i = 0
        days = [0]
        while i < len(maps):
            act = maps[i].date
            if i != 0:
                days.append((act - ant).value)
            ant = act
            i += 1
        return days

    def cropImageNmiddle(self, img_exp, aux, numDays):
        ret = None
        if numDays > 0.25:
            width = img_exp.shape[1]
            pto = int(getDegreesFromNDays(numDays, width))
            pto += aux * numDays
            ini = int((width - pto) / 2)
            ret = img_exp[0:width, int(ini - 1): int((ini - 1) + pto)]
        return ret

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if ss is not None and comm is not None:
            if mmap.getSeq():
                aux = int(float(comm.pop(0)))

                # Resample
                maps = [elem.resample((512, 512) * u.pix) for elem in ss]

                # Mapping
                maps = [sunpy.map.Map(self.equ(elem, comm), elem.meta) for elem in maps]  # *15

                # Dating
                days = self.getElapsedTime(maps)
                print("El array de dias transcurridos entre imagenes es: ", days)

                # Cropping
                crops = [self.cropImageNmiddle(maps[i].data, aux, days[i]) for i in range(len(maps))]
                crops = list(filter(lambda x: x is not None, crops))

                # Merge crops
                #final = crops.pop(0)
                final = maps.pop(0)
                for elem in maps:
                    final = np.concatenate((elem, final), axis=1)

                mmap.setSeq(False)
                mmap.setMap(sunpy.map.Map(final, ss[0].meta))  # TODO cambiar parametros meta

            else:
                gg = ss.resample((512, 512) * u.pix)
                mmap.setMap(sunpy.map.Map(self.equ(gg, comm), ss.meta))

        else:
            print("You have to load a Fits image before.")

