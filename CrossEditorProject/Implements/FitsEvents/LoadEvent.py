import sunpy.map
from Implements.Event import Event
from sunpy.data.sample import AIA_171_IMAGE
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class LoadFITSEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Load : Load a FITS image from path using file path"

    def execute(self, mmap, comm):
        try:

            if not comm:
                print(self.getDescription())
            else:
                path = comm.pop(0)
                if path == "sample":
                    mmap.setSeq(False)
                    ss = sunpy.map.Map(AIA_171_IMAGE)
                    mmap.setMap(ss)
                # Si existe una path real, mirar si es un directorio o no.
                elif not os.path.isdir(path):
                    mmap.setSeq(False)
                    ss = sunpy.map.Map(path)
                    mmap.setMap(ss)
                else:
                    seq = sunpy.map.Map(path, sequence=True)

                    seq.all_maps_same_shape()
                    mmap.setSeq(True)
                    mmap.setMap(seq)


        except KeyError:
            print("Use kwargs as ..execute(path= 'path/example')")
        except RuntimeError:
            print("Not find fits file into the path")
