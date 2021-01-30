import matplotlib.pyplot as plt
from Implements.Event import Event
from mpl_toolkits.axes_grid1 import make_axes_locatable


class ViewSelectiveEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Show : Show the current Fits image above values."

    def execute(self, mmap, comm):

        if not comm:
            print(self.getDescription())
        elif mmap.getImg() is not None:
            val = float(comm.pop(0))
            img = mmap.getImg()
            img[img < val] = 0
            fig = plt.figure()
            # Provide the Map as a projection, which creates a WCSAxes object
            ax = plt.subplot()
            im = ax.imshow(img, **mmap.getVisualParams())
            # Prevent the image from being re-scaled while overplotting.
            ax.set_autoscale_on(False)
            # Set title.
            ax.set_title('Fits image')
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('right', size='4%', pad=0.2)
            fig.colorbar(im, cax=cax, orientation='vertical')
            plt.show()


        elif mmap.getImg() is None:
            print("You have to load the file fits before")
