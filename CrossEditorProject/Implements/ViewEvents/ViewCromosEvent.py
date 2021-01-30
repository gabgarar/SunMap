import matplotlib.pyplot as plt
from astropy import units as u
from matplotlib import patches
from Implements.Event import Event
from mpl_toolkits.axes_grid1 import make_axes_locatable

from Implements.ViewEvents.Toppings import getCromos


class ViewCromosEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " ShowLimb : Show the current Fits image with a circle limb."

    def execute(self, mmap, comm):

        if mmap.getImg() is not None:
            fig = plt.figure()
            # Provide the Map as a projection, which creates a WCSAxes object
            ax = plt.subplot()
            im = ax.imshow(mmap.getImg(), **mmap.getVisualParams())
            # Prevent the image from being re-scaled while overplotting.
            ax.set_autoscale_on(False)
            # Set title.
            ax.set_title('Fits image')

            ##

            ax.add_artist(getCromos(mmap.getRSun(), mmap.getCenter()))
            ##
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('right', size='4%', pad=0.2)
            fig.colorbar(im, cax=cax, orientation='vertical')
            plt.show()


        elif mmap.getImg() is None:
            print("You have to load the file fits before")
