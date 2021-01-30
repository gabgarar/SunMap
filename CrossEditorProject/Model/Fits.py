import numpy as np
import matplotlib.pyplot as plt
import sunpy.map
from Utils.utils import init, rescale
from time import time


class Fits(object):

    def __init__(self):
        self.update = False
        self.map = None
        self.img = None
        self.stats = None
        self.normalized = False
        self.isSeq = False

    def reboot(self):
        self.update = False
        self.map = None
        self.img = None
        self.stats = None
        self.isSeq = False

    def getNormalized(self):
        return self.normalized

    def changeNormalized(self):
        self.normalized = not self.normalized

    def setMap(self, mmap):
        self.map = mmap

        if not self.isSeq:
            tiempo_inicial = time()
            self.map = self.initSetMap(self.map)
            tiempo_final = time()
            tiempo_ejecucion = tiempo_final - tiempo_inicial
            print("El tiempo total de ejecucion es: ", tiempo_ejecucion, " segundos.")
        else:
            self.map = [self.initSetMap(elem) for elem in self.map]

        self.update = True

    def initSetMap(self, mm):
        inter = mm.data.dtype
        if mm.meta['CUNIT2'] == "Sine Latitude":
            mm.meta['CUNIT2'] = 'degree'
            mm.meta['CDELT2'] = 180 / np.pi * mm.meta['CDELT2']
            mm.meta['CDELT1'] *= -1
        mm = sunpy.map.Map(init(mm.data), mm.meta)
        return mm

    def getRSun(self):
        return np.round((self.map.rsun_obs / self.map.scale[0]).value)

    def getCenter(self):
        dims = self.map.dimensions
        return [np.round(dims[0] / 2).value, np.round(dims[0] / 2).value]

    def isUpdate(self):
        return self.update

    def setIsUpdate(self, val):
        self.update = val

    def getImg(self):
        if self.isSeq:
            return self.map[0].data
        else:
            return self.map.data

    def getVisualParams(self):
        return self.map.plot_settings

    def getColorMap(self):
        return self.map.plot_settings['cmap']

    def getMap(self):
        return self.map

    def setStats(self, st):
        self.stats = st

    def getStats(self):
        if self.isSeq:
            mm = self.map[0]
        else:
            mm = self.map
        return {'type': mm.data.dtype,
             'max': np.max(mm.data), 'min': np.min(mm.data),
             'mean': np.mean(mm.data), 'std': np.std(mm.data),
             'percentile25': np.percentile(mm.data, 25),
             'percentile50': np.percentile(mm.data, 50),
             'percentile75': np.percentile(mm.data, 75),
             'percentile100': np.percentile(mm.data, 100)
             }

    def setSeq(self, sel):
        self.isSeq = sel

    def getSeq(self):
        return self.isSeq

    def getCards(self):
        if self.isSeq:
            ss = self.map[0]
        else:
            ss = self.map
        struct = ss.fits_header.tostring(sep=',', endcard=True, padding=True).split(",")
        hh = []
        i = 0
        for elem in struct:
            hh.append(elem.strip().split("="))
        return hh

    def sayHey(self):
        return "HEY"
