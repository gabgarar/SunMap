from Implements.Event import Event
import os
from scipy import misc


class SaveFITSEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Save : Save a FITS image"

    def execute(self, mmap, comm):
        pathSave = "\Out\Images"

        if mmap.getImg() is None:
            print("You have to load a Fits image before.")
        else:
            misc.imsave('out.png', mmap.getImg())
