class Hist(object):

    def __init__(self):
        self.history = []
        self.actual = -1

    def reboot(self):
        self.history = []
        self.actual = -1

    def getHistory(self):
        return self.history

    def printHist(self):
        i = 0
        print("****** HISTORY ******")
        print("actual -> {}".format(self.actual))
        for elem in self.history:
            print("[{}]".format(i))
            i += 1

    def getActual(self):
        return self.actual

    def setValueInHist(self, valor):
        print("LEN HIS {}".format(len(self.history)))
        self.actual += 1
        if len(self.history) == self.actual:
            self.history.append(valor)
        else:
            self.history = self.history[:self.actual + 1]
            self.history[self.actual] = valor

    def undo(self):
        if self.actual > 0:
            self.actual -= 1
            return self.history[self.actual]
        else:
            print("nothing to undo")
            return None

    def redo(self):
        if self.actual + 1 < len(self.history):
            self.actual += 1
            return self.history[self.actual]
        else:
            print("nothing to REDO")
            return None


