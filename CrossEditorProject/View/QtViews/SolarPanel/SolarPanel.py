import threading

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.animation import TimedAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.ticker as ticker
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

from Implements.ViewEvents.Toppings import applyToppings

import matplotlib as mpl
mpl.rcParams['text.color'] = 'White'

class SolarPanel(QWidget):
    def __init__(self, Ctrl, MainWindow):
        QWidget.__init__(self)
        self.init = False
        # Ctrl and add as observer.
        self.ctrl = Ctrl
        Ctrl.addObserver(self)
        self.canvas = CustomFigCanvas(self.ctrl, None)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet('color: White;')
        self.mainWindow = MainWindow

        self.setStyleSheet("background-color: #323232")
        ll = QVBoxLayout()

        self.ww = QWidget()
        self.ww.setStyleSheet("background-color: #000000;")
        self.ww.setMinimumSize(QtCore.QSize(700, 550))
        ll.addWidget(self.toolbar)
        ll.addWidget(self.ww)
        self.setLayout(ll)

    def updateViewer(self, fits, ret):
        th = threading.Thread(target=self.refresh(fits, ret))
        th.start()

    def refresh(self, fits, ret):
        if fits:
            self.ww.setVisible(False)
            if self.canvas.isAnim():
                self.canvas.event_source.stop()
            self.layout().removeWidget(self.canvas)
            self.layout().removeWidget(self.toolbar)
            if not fits.getSeq():
                self.canvas = CustomFigCanvas(self.ctrl, fits)
                self.toolbar = NavigationToolbar(self.canvas, self)
                self.toolbar.setStyleSheet('color: White;')
            else:
                self.canvas = CustomFigCanvasAnimated(self.ctrl, fits)
                self.toolbar = NavigationToolbar(self.canvas, self)
                self.toolbar.setStyleSheet('color: White;')

            self.layout().addWidget(self.toolbar)
            self.layout().addWidget(self.canvas)
        else:
            raise ValueError()


####################################################### UNIQUE #################################################
class CustomFigCanvas(FigureCanvas):

    def __init__(self, Ctrl, fits):

        self.anim = False
        # Data.
        self.fits = fits
        if self.fits is not None:
            self.maps = fits.getMap()

        # Figure.
        self.fig = Figure(figsize=(10, 10), dpi=100)
        self.fig.patch.set_facecolor('#000000')

        # Axis.
        self.ax = self.fig.add_subplot(111)
        self.ax.spines['bottom'].set_color('#c9c9c9')
        self.ax.spines['top'].set_color('#c9c9c9')
        self.ax.spines['left'].set_color('#c9c9c9')
        self.ax.spines['right'].set_color('#c9c9c9')
        self.ax.xaxis.label.set_color('#c9c9c9')
        self.ax.yaxis.label.set_color('#c9c9c9')
        self.ax.tick_params(axis='x', colors='#c9c9c9')
        self.ax.tick_params(axis='y', colors='#c9c9c9')

        if self.fits is not None:
            scale_x = self.maps.meta["CDELT1"]
            center_x = int(self.maps.data.shape[0] / 2)
            center_y = int(self.maps.data.shape[1] / 2)
            centerArc_x = center_x * scale_x
            centerArc_y = center_y * scale_x

            if self.maps.meta['CUNIT1'] == 'arcsec':
                self.ax.get_xaxis().set_major_formatter(
                    ticker.FuncFormatter(lambda x, p: '{:.0f}″'.format(x * scale_x - centerArc_x)))
                self.ax.set_xticks(self.calcArcPoints(center_x, self.maps.data.shape[1]))
            elif self.maps.meta['CUNIT1'] == 'deg':
                dif = self.maps.meta['DD']
                scale = 360 * dif / 27.2753
                scale_x = scale / self.maps.data.shape[1]

                center_x = int(self.maps.data.shape[1] / 2)
                centerArc_x = center_x * scale_x
                self.ax.get_xaxis().set_major_formatter(
                    ticker.FuncFormatter(lambda x, p: '{:.0f}$^o$'.format(x * scale_x - centerArc_x)))
                self.ax.set_xticks(self.calcDegXXPoints(center_x, self.maps.data.shape[1], scale_x))

                # Y AXIS. -> VERTICAL ''
            if self.maps.meta['CUNIT2'] == 'arcsec':
                self.ax.get_yaxis().set_major_formatter(
                    ticker.FuncFormatter(lambda y, p: '{:.0f}″'.format(y * scale_x - centerArc_y)))
                self.ax.set_yticks(self.calcArcPoints(center_y, self.maps.data.shape[0]))

            elif self.maps.meta['CUNIT2'] == 'deg':
                sc = 90 / (self.maps.meta['R_SUN'])
                center_y = int(self.maps.data.shape[0] / 2)  # 1
                centerArc_y = center_y * sc
                self.ax.get_yaxis().set_major_formatter(
                    ticker.FuncFormatter(lambda y, p: '{:.1f}'.format(
                        np.sin(np.pi * (np.round(y * sc - centerArc_y)) /180)
                        #np.round(y * sc - centerArc_y))
                    )))
                
                
                self.ax.set_yticks(self.calcDegPoints(center_y, self.maps.data.shape[0]))
                self.ax.set_ylabel("sin(latitude)")
                self.ax.set_ylabel("longitude")

            #############

        # Canvas and Animation.
        FigureCanvas.__init__(self, self.fig)

        if self.fits is not None:
            self.plot()
            self.updateGeometry()

    def calcArcPoints(self, center, lim):
        ranks = list()
        ini_izq = ini_der = center
        ranks.append(center)  # Añado el punto 0
        while ini_der < lim:
            ranks.append(ini_der + int(250 / self.maps.meta["CDELT1"]))
            ranks.append(ini_izq - int(250 / self.maps.meta["CDELT1"]))
            ini_izq -= int(250 / self.maps.meta["CDELT1"])
            ini_der += int(250 / self.maps.meta["CDELT1"])
        return ranks

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

    def calcDegPoints(self, center, lim):
        ranks = list()
        ini_izq = ini_der = center
        sc = 90 / self.maps.meta['R_SUN']
        ranks.append(center)
        while ini_der < lim:
            ranks.append(ini_der + int(30 / sc))
            ranks.append(ini_izq - int(30 / sc))
            ini_izq -= int(30 / sc)
            ini_der += int(30 / sc)
        return ranks

    def stop(self):
        pass

    def isAnim(self):
        return self.anim

    def plot(self):

        label = 'Date:  {0}'.format(self.maps.meta["DATE-OBS"])


        im = self.ax.imshow(self.maps.data, **self.fits.getVisualParams())  # resample=[0.5, 0.5]

        applyToppings(self.maps.data, self.fits.getRSun(), self.fits.getCenter(), self.ax)

        self.ax.set_autoscale_on(False)


####################################################### ANIMATION ######################################################

class CustomFigCanvasAnimated(FigureCanvas, TimedAnimation):

    def __init__(self, Ctrl, fits):

        self.anim = True
        # Data.
        self.fits = fits
        self.maps = fits.getMap()
        self.maps = [elem.resample((1024, 1024) * u.pix) for elem in self.maps]

        # Figure.
        self.fig = Figure(figsize=(10, 10), dpi=100)
        self.fig.patch.set_facecolor('#000000')

        # Axis.
        self.ax = self.fig.add_subplot(111)
        self.ax.spines['bottom'].set_color('#c9c9c9')
        self.ax.spines['top'].set_color('#c9c9c9')
        self.ax.spines['left'].set_color('#c9c9c9')
        self.ax.spines['right'].set_color('#c9c9c9')
        self.ax.xaxis.label.set_color('#c9c9c9')
        self.ax.yaxis.label.set_color('#c9c9c9')
        self.ax.tick_params(axis='x', colors='#c9c9c9')
        self.ax.tick_params(axis='y', colors='#c9c9c9')

        if self.fits is not None:
            scale_x = self.maps[0].meta["CDELT1"]
            center_x = int(self.maps[0].data.shape[0] / 2)
            center_y = int(self.maps[0].data.shape[1] / 2)
            centerArc_x = center_x * scale_x
            centerArc_y = center_y * scale_x

            if self.maps[0].meta['CUNIT1'] == 'arcsec':
                self.ax.get_xaxis().set_major_formatter(
                    ticker.FuncFormatter(lambda x, p: '{:.0f}″'.format(x * scale_x - centerArc_x)))
                self.ax.set_xticks(self.calcArcPoints(center_x, self.maps[0].data.shape[0]))

            if self.maps[0].meta['CUNIT2'] == 'arcsec':
                self.ax.get_yaxis().set_major_formatter(
                    ticker.FuncFormatter(lambda y, p: '{:.0f}″'.format(y * scale_x - centerArc_y)))
                self.ax.set_yticks(self.calcArcPoints(center_y, self.maps[0].data.shape[1]))

        # Canvas and Animation.
        FigureCanvas.__init__(self, self.fig)
        TimedAnimation.__init__(self, self.fig, interval=2500, repeat=True, blit=True)

        self.updateGeometry()

    def calcArcPoints(self, center, lim):
        ranks = list()
        ini_izq = ini_der = center
        ranks.append(center)  # Añado el punto 0
        while ini_der < lim:
            ranks.append(ini_der + int(250 / self.maps[0].meta["CDELT1"]))
            ranks.append(ini_izq - int(250 / self.maps[0].meta["CDELT1"]))
            ini_izq -= int(250 / self.maps[0].meta["CDELT1"])
            ini_der += int(250 / self.maps[0].meta["CDELT1"])
        return ranks

    def _draw_frame(self, framedata):
        if self.fits:
            if self.fits.getSeq():
                i = framedata
                self.frames = np.arange(0, len(self.maps))
                label = 'Date:  {0}'.format(self.maps[i].meta["DATE-OBS"])

                im = self.ax.imshow(self.maps[i].data, **self.maps[i].plot_settings)

                applyToppings(self.maps[i].data, self.getRSun(self.maps[i]), self.getCenter(self.maps[i]), self.ax)

                self.ax.set_autoscale_on(False)
                return None, self.ax

    def getRSun(self, map):
        return np.round((map.rsun_obs / map.scale[0]).value)

    def getCenter(self, map):
        dims = map.dimensions
        return [np.round(dims[0] / 2).value, np.round(dims[0] / 2).value]

    def stop(self):
        self._stop()

    def new_frame_seq(self):
        if self.fits and self.fits.getSeq():
            return iter(range(len(self.maps)))

    def _init_draw(self):
        pass

    def isAnim(self):
        return self.anim
