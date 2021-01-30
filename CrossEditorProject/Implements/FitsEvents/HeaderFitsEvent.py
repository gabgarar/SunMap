import numpy as np
from Implements.Event import Event


class HeaderFitsEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Header : Header cards of a FITS image"

    def execute(self, mmap, comm):
        if mmap.getMap() is None:
            print("You have to load the file fits before")
        else:
            for elem in mmap.getCards():
                print(elem)
            return mmap.getCards()






