from skimage import img_as_float64, img_as_float

from Implements.Event import Event
import numpy as np
from scipy import ndimage


class SobelFilterEvent(Event):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Sobel : Sobel filter. "

    def execute(self, mmap, comm):

        if mmap.getImg() is not None:
            img = mmap.getImg().copy()
            dx = ndimage.sobel(img, axis=0, mode='nearest')
            dy = ndimage.sobel(img, axis=1, mode='nearest')
            sobel = np.hypot(dx, dy)

            mmap.setImg(sobel)
            mmap.setIsUpdate(True)
