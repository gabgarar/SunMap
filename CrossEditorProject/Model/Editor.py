
from Model.Fits import Fits
from Model.Hist import Hist
from Model.Observers.Observed import Observed


class Editor(Observed):

    # Constructor.
    def __init__(self):
        self.eventList = []
        self.fits = Fits()
        self.hist = Hist()
        self.observers = []

    # Observer functions.
    def setEvent(self, event):
        self.eventList.append(event)

    def addObserver(self, obs):
        self.observers.append(obs)

    def removeObserver(self, obs):
        self.observers.remove(obs)

    def reboot(self):
        raise NotImplementedError()

    def updateViewers(self, ret):
        for obs in self.observers:
            obs.updateViewer(self.fits, ret)

    # Execution.
    def execute(self, comm):
        ret = None
        for elem in self.eventList:
            if elem.getCommand() == "undo" or elem.getCommand() == "redo":
                comm = {'unre': self.hist}
            elif elem.getCommand() == "reboot":
                comm = {'hist': self.hist, 'fits': self.fits}
            ret = elem.execute(self.fits, comm)
            self.eventList.pop(0)
            if self.fits.isUpdate():
                self.hist.setValueInHist(self.fits.getMap())
                self.updateViewers(ret)
                self.fits.setIsUpdate(False)
        return ret

            #self.hist.printHist()

    def getFits(self):
        return self.fits


