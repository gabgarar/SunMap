from Implements.Event import Event
import sunpy.map
import sunpy.sun
import squircle
import astropy.units as u
from numba import jit, cuda


class TransformEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Polar transform : Apply the transformation to the image."

    @jit
    def equ(self, imgData, comm):
        return squircle.to_square(imgData, method="fgs")

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if ss is not None and comm is not None:
            if mmap.getSeq():
                maps = [elem.resample((512, 512) * u.pix) for elem in ss]
                maps = [sunpy.map.Map(self.equ(elem.data, comm), elem.meta) for elem in maps]
                mmap.setMap(maps)
            else:
                gg = ss.resample((512, 512) * u.pix)
                mmap.setMap(sunpy.map.Map(self.equ(gg.data, comm), ss.meta))

        else:
            print("You have to load a Fits image before.")
