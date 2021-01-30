import math
import numpy as np
from scipy import ndimage
from Implements.Event import Event


class StaticFilters(Event):
    conj = {
        'average':
            [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
        ,
        'underMild':
            [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
        ,
        'identity':
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        ,
        'soft':
            [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
        ,
        # Gradient Based
        # both gradX and gradY will be very sensitive to noise
        'gradX':
            [[-1, 1]]
        ,
        'gradY':
            [[-1], [1]]
        ,
        # A little bit sensibility
        'roberts':
            [[0, -1], [1, 0]]
        ,
        'robertsInv':
            [[-1, 0], [0, 1]]
        ,
        # Prewitt better detect horizontal and vertical edges
        'prewittX':
            [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
        ,
        'prewittY':
            [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
        ,
        # Sobel better detect diagonals
        'sobelX':
            [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        ,
        'sobelY':
            [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
        ,
        # Isotropic look for a balance between both
        'isoX':
            [[-1, 0, 1], [-math.sqrt(2), 0, math.sqrt(2)], [-1, 0, 1]]
        ,
        'isoY':
            [[-1, -math.sqrt(2), -1], [0, 0, 0], [1, math.sqrt(2), 1]]
        ,
        # Laplacian
        'lapX':
            [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
        ,
        'lapY':
            [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]

    }

    def getMatrix(self, key):
        return self.conj[key]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Convu : Use a convolutional filter"

    def execute(self, mmap, comm):
        try:
            if mmap.getImg() is not None:
                if not comm:
                    print("You have to indicate which filter you want to use")
                else:
                    tp = str(mmap.getImg().dtype)
                    if tp != "float32" and tp != "float64":
                        mat = self.getMatrix(str(comm.pop(0)))
                        kernel = np.asarray(mat)
                        print(kernel)
                        api = ndimage.convolve(mmap.getImg(), kernel, mode='nearest')
                        if comm and comm.pop(0) == "rest":
                            api = mmap.getImg() - ndimage.convolve(mmap.getImg(), kernel, mode='nearest')
                        mmap.setImg(api)
                        mmap.setIsUpdate(True)
                    else:
                        print("Convu not admit float struct.")
            else:
                print("You have to load the file fits before")
        except KeyError:
            print("The filter you want to use is not available.")
