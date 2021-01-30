from abc import abstractmethod


class Observed:

    @abstractmethod
    def addObserver(self, obs):
        pass

    @abstractmethod
    def removeObserver(self, obs):
        pass

    @abstractmethod
    def reboot(self):
        pass

    @abstractmethod
    def updateViewers(self, ret):
        pass

