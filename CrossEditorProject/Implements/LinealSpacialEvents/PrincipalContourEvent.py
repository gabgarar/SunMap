from scipy import ndimage
from skimage import measure
import sunpy
import matplotlib.pyplot as plt
from Implements.Event import Event
import numpy as np
from Utils.utils import getMaxValue


def binary(val, imgData):
    if 0 <= val <= 100:
        pp = np.percentile(imgData, val)
        img = imgData.copy()
        dd = getMaxValue(img.dtype)
        img[img < pp] = dd[0]
        img[img >= pp] = dd[1]
        return img
    else:
        print("You have to load a Fits image before.")


class PrincipalContourEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Principal Contour : Principal contours of a FITS image."

    def conts(self, val, r, imgData, plot_sets):
        img = imgData.copy()  # cuidado con los punteros
        img = binary(val, imgData)
        img = ndimage.gaussian_filter(img, r)

        contours = measure.find_contours(img, 0.8, fully_connected="low")
        i = 0
        # Display the image and plot all contours found
        fig, ax = plt.subplots()
        ax.imshow(imgData, **plot_sets)
        for n, contour in enumerate(contours):
            cont = np.shape(contour)[0]
            if cont > 300:
                ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if not comm or len(comm) < 2:
            print(self.getDescription())
        elif ss is not None:
            val = float(comm.pop(0))
            r = float(comm.pop(0))

            if mmap.getSeq():
                [self.conts(val, r, elem.data, elem.plot_settings) for elem in ss]
            else:
                self.conts(val, r, ss.data, mmap.getVisualParams())
        else:
            print("You have to load a Fits image before.")
