from abc import abstractmethod


class GeneralObserverViewer:

    @abstractmethod
    def updateViewer(self, Fits, ret):
        pass

    def reportError(self):
        pass

    def addEvent(self):
        pass

    def reboot(self):
        pass
