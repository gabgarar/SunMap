from Implements.Event import Event
import sunpy.map
import sunpy.sun
import squircle
import astropy.units as u
from numba import jit, cuda
import numpy as np
import matplotlib.pyplot as plt

def getDegreesFromNDays(numDays, width):
    T = 27.28
    deg = numDays * 360 / T
    numPixInImage = deg * width / 180
    return numPixInImage


class SynopticEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Synoptic Map : Apply the transformation to the image."

    @jit
    def equ(self, imgData, comm):
        return squircle.to_square(imgData, method="fgs")

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
                ini = ss[0].data.shape[1]

                # Resample
                resample = 1024
                maps = [elem.resample((resample, resample) * u.pix) for elem in ss]
                #maps = [elem for elem in ss]
                # Mapping
                maps = [sunpy.map.Map(self.equ(elem.data, comm), elem.meta) for elem in maps] # *15

                # Dating
                days = self.getElapsedTime(maps)
                print("El array de dias transcurridos entre imagenes es: ", days)

                # Cropping
                crops = [self.cropImageNmiddle(maps[i].data, aux, days[i]) for i in range(len(maps))]
                crops = list(filter(lambda x: x is not None, crops))

                # Merge crops
                final = crops.pop(0)
                for elem in crops:
                    final = np.concatenate((elem, final), axis=1)

                mmap.setSeq(False)
                ss[0].meta['CUNIT1'] = "deg"
                ss[0].meta['CUNIT2'] = "deg"
                print(f"EL tamaño de la imagen inicial es de : {ini}")

                print("yeyeyey: ", np.sum(days))
                ss[0].meta['DD'] = np.sum(days)

                ss[0].meta['R_SUN'] = resample * ss[0].meta['R_SUN'] / ini
                print(f"El nuevo tamaño del radio del sol es de : {ss[0].meta['R_SUN']} pixeles")

                print("Se cambia a : ", ss[0].meta['CUNIT1'])

                mmap.setMap(sunpy.map.Map(final, ss[0].meta))



            else:
                resample = 512
                ini = ss.data.shape[0]
                gg = ss.resample((resample, resample) * u.pix)
                ss.meta['CUNIT1'] = "arcsec"
                ss.meta['CUNIT2'] = "arcsec"
                ss.meta['R_SUN'] = resample * ss.meta['R_SUN'] / ini
                print("Se cambia a : ", ss.meta['CUNIT1'])
                mmap.setMap(sunpy.map.Map(self.equ(gg.data, comm), ss.meta))

        else:
            print("You have to load a Fits image before.")
