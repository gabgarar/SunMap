import numpy as np
import matplotlib.pyplot as plt
import cmapy
import cv2
from Implements.Event import Event


class ViewGradientEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Colormap : Show colormap using in actual Fits image."

    def execute(self, mmap, comm):

        if mmap.getImg() is not None:
            im_size = 255
            img = np.zeros((im_size, im_size, 3), np.uint8)

            # Draw a vertical gradient using the 'hot' colormap.
            for i in range(im_size):
                color = cmapy.color(mmap.getColorMap(), float(i) / im_size)
                img[i, :, :] = color
            color = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

            plt.imshow(color)
            plt.show()

        elif mmap.getImg() is None:
            print("You have to load the file fits before")

