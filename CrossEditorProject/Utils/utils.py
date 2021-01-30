from skimage import exposure
from skimage.util import *
import numpy as np


def getMaxValue(inter):
    if inter == "float64" or inter == "float32" or inter == "float":
        return 0, 1
    else:
        return np.iinfo(inter).min, np.iinfo(inter).max


def rescale(img):
    inter = img.dtype

    range = getMaxValue(inter)

    rescaled = exposure.rescale_intensity(img, out_range=range)
    del img
    return rescaled


def init(img):
    return cast(img, None)


def cast(img, val):  # image.dtype -> dtype

  
    if img.dtype != val:
        if val is not None:
            img = rescale(img)
        else:
            val = img.dtype

        if val == "uint8" or val == "int8":
            casted = img_as_ubyte(img)
            del img
        else:
            casted = img_as_uint(img)
            del img
        return casted
    else:
        return img
