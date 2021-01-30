from PyQt5.QtWidgets import QInputDialog
from matplotlib import patches
from scipy import ndimage
import numpy as np
from skimage import measure
from Utils.utils import getMaxValue

import matplotlib.pyplot as plt

params = {
    "printLimb": False,
    "printCromos": False,
    "printContours": False,
    "hideAxis": False,
    "printGrid": False,
    "saveFig": False
}


def getParams():
    return params


def getAtt(elem):
    return params[elem]


def setAtt(elem):
    params[elem] = not params[elem]
    print("Elem :", params[elem])


def printVisualParams():
    print(params)


def saveFig(ax, i):
    ss = False
    if not params['hideAxis']:
        params['hideAxis'] = True
        hideAxis(ax, i)
        ss = True
    plt.gcf()
    path = "../Test/SavesSequence/saveSeq" + str(i) + ".png"
    plt.savefig(path, quality=100, optimize=True)
    if ss:
        params['hideAxis'] = False


def hideAxis(ax, i):
    ax.set_axis_off()
    ax.set_title("")
    if params['hideAxis']:
        ax.axis('off')
    else:
        ax.axis('on')


def printGrid(ax):
    if params['printGrid']:
        ax.set_axisbelow(params['printGrid'])
        ax.yaxis.grid(color='#c9c9c9', linestyle='dashed')
        ax.xaxis.grid(color='#c9c9c9', linestyle='dashed')


def getLimb(rad, center):
    c_kw = {
        'fill': False,
        'color': '#c9c9c9',
        'zorder': 100,
        'radius': rad
    }
    circ = patches.Circle(center, **c_kw)
    return circ


def getCromos(rad, center):
    c_kw = {
        'fill': True,
        'color': 'black',
        'zorder': 100,
        'radius': rad
    }
    circ = patches.Circle(center, **c_kw)
    return circ


def getContours(img, ax):
    return conts(99, 13, img, "gray", ax)


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


def conts(val, r, imgData, plot_sets, ax):
    img = imgData.copy()
    img = binary(val, imgData)
    img = ndimage.gaussian_filter(img, r)

    contours = measure.find_contours(img, 1, fully_connected="low")
    i = 0

    for n, contour in enumerate(contours):
        cont = np.shape(contour)[0]
        if cont > 500:
            ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
    return ax


def applyToppings(img, radius, center, ax):
    i = 0
    if getAtt("printCromos"):
        ax.add_artist(getCromos(radius, center))

    if getAtt("printLimb"):
        ax.add_artist(getLimb(radius, center))

    if getAtt("hideAxis"):
        hideAxis(ax, i)

    if getAtt("printGrid"):
        printGrid(ax)

    if getAtt("printContours"):
        getContours(img, ax)
