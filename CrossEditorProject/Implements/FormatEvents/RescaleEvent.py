from skimage import exposure
from Implements.Event import Event


class RescaleEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Rescale : Rescale a FITS image "

    def execute(self, mmap, comm):
        if mmap.getImg() is not None:
            range = None
            inter = mmap.getImg().dtype

            if inter == "uint16":
                range = (0, 2 ** 16 - 1)
            elif inter == "uint8":
                range = (0, 2 ** 8 - 1)
            elif inter == "uint32":
                range = (0, 2 ** 32 - 1)
            elif inter == "float" or inter == "float32" or inter == "float64":
                range = (0, 1)
            else:
                range = (0, 2 ** 8 - 1)

            rescaled = exposure.rescale_intensity(mmap.getImg(), out_range=range)
            mmap.setIsUpdate(True)
            mmap.setImg(rescaled)
            mmap.changeNormalized()

        else:
            print("You have to load the file fits before")
