from Implements.Event import Event
import os
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class SaveFITSEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Save : Save a FITS image"
        
    def calcDegXXPoints(self, center, lim, sc):
        ranks = list()
        ini_izq = ini_der = center
        ranks.append(center)
        while ini_der < lim:
            ranks.append(ini_der + int(60 / sc))
            ranks.append(ini_izq - int(60 / sc))
            ini_izq -= int(60 / sc)
            ini_der += int(60 / sc)
        return ranks

    def calcDegPoints(self, center, lim, maps):
        ranks = list()
        ini_izq = ini_der = center
        sc = 90 / maps.meta['R_SUN']
        ranks.append(center)
        while ini_der < lim:
            ranks.append(ini_der + int(30 / sc))
            ranks.append(ini_izq - int(30 / sc))
            ini_izq -= int(30 / sc)
            ini_der += int(30 / sc)
        return ranks

    def calcArcPoints(self, center, lim, maps):
        ranks = list()
        ini_izq = ini_der = center
        ranks.append(center)  # Añado el punto 0
        while ini_der < lim:
            ranks.append(ini_der + int(250 / maps.meta["CDELT1"]))
            ranks.append(ini_izq - int(250 / maps.meta["CDELT1"]))
            ini_izq -= int(250 / maps.meta["CDELT1"])
            ini_der += int(250 / maps.meta["CDELT1"])
        return ranks

    def execute(self, mmap, comm):
        pathSave = "\Out\Images"
        if mmap.getImg() is None:
            print("You have to load a Fits image before.")
        else:
            fig, ax = plt.subplots(figsize=(15, 15))
            
            fits = mmap
            maps = None
            if fits is not None:
                maps = fits.getMap()

            # Figure.
            
      

            if fits is not None:
                scale_x = maps.meta["CDELT1"]
                center_x = int(maps.data.shape[0] / 2)
                center_y = int(maps.data.shape[1] / 2)
                centerArc_x = center_x * scale_x
                centerArc_y = center_y * scale_x

                if maps.meta['CUNIT1'] == 'arcsec':
                    ax.get_xaxis().set_major_formatter(
                        ticker.FuncFormatter(lambda x, p: '{:.0f}″'.format(x * scale_x - centerArc_x)))
                    ax.set_xticks(self.calcArcPoints(center_x, maps.data.shape[1], maps))
                elif maps.meta['CUNIT1'] == 'deg':
                    dif = maps.meta['DD']
                    scale = 360 * dif / 27.2753
                    scale_x = scale / maps.data.shape[1]

                    center_x = int(maps.data.shape[1] / 2)
                    centerArc_x = center_x * scale_x
                    ax.get_xaxis().set_major_formatter(
                        ticker.FuncFormatter(lambda x, p: '{:.0f}º'.format(x * scale_x - centerArc_x)))
                    ax.set_xticks(self.calcDegXXPoints(center_x, maps.data.shape[1], scale_x))

                    # Y AXIS. -> VERTICAL ''
                if maps.meta['CUNIT2'] == 'arcsec':
                    ax.get_yaxis().set_major_formatter(
                        ticker.FuncFormatter(lambda y, p: '{:.0f}″'.format(y * scale_x - centerArc_y)))
                    ax.set_yticks(self.calcArcPoints(center_y, maps.data.shape[0], maps))

                elif maps.meta['CUNIT2'] == 'deg':
                    sc = 90 / (maps.meta['R_SUN'])
                    center_y = int(maps.data.shape[0] / 2)  # 1
                    centerArc_y = center_y * sc
                    ax.get_yaxis().set_major_formatter(
                        ticker.FuncFormatter(lambda y, p: '{:.0f}º'.format(y * sc - centerArc_y)))  # 2.5 para HMI
                    ax.set_yticks(self.calcDegPoints(center_y, maps.data.shape[0], maps))
                    
                    
                    
                # save figure
                
                ax.imshow(maps.data, cmap='stereocor1')
                print("COMM: ", comm)
                plt.savefig(comm[0])

