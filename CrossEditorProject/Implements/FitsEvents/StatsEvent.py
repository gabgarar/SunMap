import numpy as np
from Implements.Event import Event


class StatsEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Stats : Statistics of a FITS image"

    def execute(self, mmap, comm):
        ret = None
        if mmap.getMap() is None:
            print("You have to load the file fits before")
        else:

            stats = {'type': mmap.getImg().dtype,
                     'max': np.max(mmap.getImg()), 'min': np.min(mmap.getImg()),
                     'mean': np.mean(mmap.getImg()), 'std': np.std(mmap.getImg()),
                     'percentile25': np.percentile(mmap.getImg(), 25),
                     'percentile50': np.percentile(mmap.getImg(), 50),
                     'percentile75': np.percentile(mmap.getImg(), 75),
                     'percentile100': np.percentile(mmap.getImg(), 100)
                    }
            for elem in stats:
                print("{:20} : {}".format(elem, stats[elem]))
            ret = stats

        return ret


