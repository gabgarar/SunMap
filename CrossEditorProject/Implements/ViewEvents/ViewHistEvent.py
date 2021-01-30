import threading

from numpy import array
import matplotlib.pyplot as plt

from Implements.Event import Event


class ViewHistEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Hist : Show the histogram of current Fits image."

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if ss is not None and comm is not None:
            if mmap.getSeq():
                pass
                # maps = [sunpy.map.Map(self.equ(elem.data, comm), elem.meta) for elem in ss]
                # mmap.setMap(maps)
            else:
                # mmap.setMap(sunpy.map.Map(self.equ(ss.data, comm), ss.meta))
                th = threading.Thread(target=self.plotHist(mmap))
                th.start()

        else:
            print("You have to load a Fits image before.")

    def plotHist(self, mmap):
        img = mmap.getMap().data

        title = 'Date:  {0}'.format(mmap.getMap().meta["DATE-OBS"])
        x = [x for x in array(img).flat]

        self.fig, self.ax = plt.subplots()

        # the histogram of the data
        n, bins, patches = self.ax.hist(x, 150, facecolor='#50c1fa')
        self.fig.patch.set_facecolor('#000000')
        self.ax.set_title(title, color="white")

        self.ax.spines['bottom'].set_color('#c9c9c9')
        self.ax.spines['top'].set_color('#c9c9c9')
        self.ax.spines['left'].set_color('#c9c9c9')
        self.ax.spines['right'].set_color('#c9c9c9')
        self.ax.xaxis.label.set_color('#c9c9c9')
        self.ax.yaxis.label.set_color('#c9c9c9')
        self.ax.tick_params(axis='x', colors='#c9c9c9')
        self.ax.tick_params(axis='y', colors='#c9c9c9')

        plt.xlabel('Level')
        plt.ylabel('Accounting')
        plt.title(title)

        plt.grid(True)
        plt.show()
