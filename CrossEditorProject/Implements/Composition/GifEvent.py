import numpy as np
from matplotlib import ticker
from matplotlib.animation import FuncAnimation, PillowWriter
from Implements.Event import Event
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GifEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Gif : Generate a gif composition from a Fits image."

    def plotAsGif(self, maps, val):
        fig, ax = plt.subplots()
        fig.set_tight_layout(True)

        def update(i):
            label = 'Date:  {0}'.format(maps[i].meta["DATE-OBS"])
            im = ax.imshow(maps[i].data, **maps[i].plot_settings)
            ax.set_autoscale_on(False)
            ax.set_title(label)
            return None, ax

        scale_x = maps[0].meta["CDELT1"]
        center_x = int(maps[0].data.shape[0] / 2)
        center_y = int(maps[0].data.shape[0] / 2)
        centerArc_x = center_x * scale_x
        centerArc_y = center_y * scale_x

        if maps[0].meta['CUNIT1'] == 'arcsec':
            ax.get_xaxis().set_major_formatter(
                ticker.FuncFormatter(lambda x, p: '{:.0f}″'.format(x * scale_x - centerArc_x)))
            ax.set_xticks(self.calcArcPoints(center_x, maps[0].data.shape[0], maps))

        if maps[0].meta['CUNIT2'] == 'arcsec':
            ax.get_yaxis().set_major_formatter(
                ticker.FuncFormatter(lambda y, p: '{:.0f}″'.format(y * scale_x - centerArc_y)))
            ax.set_yticks(self.calcArcPoints(center_y, maps[0].data.shape[1], maps))
        ######3
        writer = animation.writers['ffmpeg']
        writer = writer(fps=30)
        anim = FuncAnimation(fig, update, interval=float(val), cache_frame_data=False, frames=np.arange(0, len(maps)))
        anim.save('animation.gif', writer='imagemagick')

    def calcArcPoints(self, center, lim, maps):
        ranks = list()
        ini_izq = ini_der = center
        ranks.append(center)  # Añado el punto 0
        while ini_der < lim:
            ranks.append(ini_der + int(250 / maps[0].meta["CDELT1"]))
            ranks.append(ini_izq - int(250 / maps[0].meta["CDELT1"]))
            ini_izq -= int(250 / maps[0].meta["CDELT1"])
            ini_der += int(250 / maps[0].meta["CDELT1"])
        return ranks

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if not comm:
            print(self.getDescription())
        elif ss is not None:
            val = comm.pop(0)
            if mmap.getSeq():
                self.plotAsGif(ss, val)

            else:
                print("You cannot do a gif with a simple image.")
