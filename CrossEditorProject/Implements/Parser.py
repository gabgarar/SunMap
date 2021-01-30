class Parser(object):

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        parsers = []

    def getNameParser(self):
        return self.name

    def getHelp(self):
        hh = []
        for i in range(len(self.parsers)):
            hh.append(self.parsers[i].getHelp())
        return {self.name: hh}

    def hasCommand(self, comm):
        ret = None
        for i in range(len(self.parsers)):
            event = self.parsers[i].hasCommand(comm)
            if event is not None:
                ret = event
        return ret
