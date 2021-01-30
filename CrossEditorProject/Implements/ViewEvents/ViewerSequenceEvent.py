import numpy as np
from matplotlib.animation import FuncAnimation
from Implements.Event import Event
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from Implements.ViewEvents.Toppings import getAtt, getLimb, getCromos, getContours, hideAxis, printGrid, saveFig


def getRSun(map):
    return np.round((map.rsun_obs / map.scale[0]).value)


def getCenter(map):
    dims = map.dimensions
    return [np.round(dims[0] / 2).value, np.round(dims[0] / 2).value]


def plotAsGif(maps, val):
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)

    def update(i):
        label = 'Date:  {0}'.format(maps[i].meta["DATE-OBS"])
        im = ax.imshow(maps[i].data, **maps[i].plot_settings, resample=[0.5, 0.5])
        ax.set_title(label)
        if getAtt("printCromos"):
            ax.add_artist(getCromos(getRSun(maps[i]), getCenter(maps[i])))

        if getAtt("printLimb"):
            ax.add_artist(getLimb(getRSun(maps[i]), getCenter(maps[i])))

        if getAtt("hideAxis"):
            hideAxis(ax, i)

        if getAtt("saveFig"):
            saveFig(ax, i)

        if getAtt("printGrid"):
            printGrid(ax)

        if getAtt("printContours"):
            getContours(maps[i], ax)

        ax.set_autoscale_on(False)
        return None, ax

    anim = FuncAnimation(fig, update, interval=val, frames=np.arange(0, len(maps)))
    plt.show()


def plotAsSimpleImg(ss, imgData, kk):
    fig = plt.figure()
    # Provide the Map as a projection, which creates a WCSAxes object
    ax = plt.subplot()
    im = ax.imshow(imgData, **kk)
    # Prevent the image from being re-scaled while overplotting.

    if getAtt("printCromos"):
        ax.add_artist(getCromos(getRSun(ss), getCenter(ss)))

    if getAtt("printLimb"):
        ax.add_artist(getLimb(getRSun(ss), getCenter(ss)))

    ax.set_autoscale_on(False)
    # Set title.
    ax.set_title('Fits image')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='4%', pad=0.2)
    fig.colorbar(im, cax=cax, orientation='vertical')
    plt.show()


class ViewerSequenceEvent(Event):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Gif : Generate a gif composition from a Fits image."

    def execute(self, mmap, comm):
        ss = mmap.getMap()

        if ss is not None:

            if mmap.getSeq():
                if not comm:
                    print(self.getDescription())
                else:
                    val = comm.pop(0)
                    plotAsGif(ss, val)
            else:
                plotAsSimpleImg(ss, ss.data, mmap.getVisualParams())

        else:
            print("You have to load a Fits image before.")
