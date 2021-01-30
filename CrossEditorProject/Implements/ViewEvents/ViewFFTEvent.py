import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from Implements.Event import Event

class ViewFFTEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " FFT : Show the fft image."

    def getSpectrumCenter(self, img):
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        return fshift
        #return 20 * np.log(np.abs(fshift))



    def getLines(self, rad, center):
        c_kw = {
            'fill': True,
            'color': 'black',
        }
        circ = patches.Rectangle(center, **c_kw)
        return circ

    def execute(self, mmap, comm):
        ss = mmap.getImg()
        if ss is not None:
            title = "FFT centered"
            fft = self.getSpectrumCenter(ss)
            fft_img = 20 * np.log(np.abs(self.getSpectrumCenter(ss)))
            #
            fig = plt.figure()
            ax = plt.subplot()
            im = ax.imshow(fft_img, cmap=mmap.getColorMap())
            # Prevent the image from being re-scaled while overplotting.
            ax.set_autoscale_on(False)
            # Set title.
            ax.set_title(title)

            plt.show()

        elif mmap.getImg() is None:
            print("You have to load the file fits before")