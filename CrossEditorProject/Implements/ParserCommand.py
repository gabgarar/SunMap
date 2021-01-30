class ParserCommand(object):

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        events = []

    def getNameParser(self):
        return self.name

    def getHelp(self):
        hh = []
        for i in range(len(self.events)):
            hh.append(self.events[i].getDescription())
        return {self.name: hh}

    def hasCommand(self, comm):
        ret = None
        for i in range(len(self.events)):
            if self.events[i].parse(comm):
                ret = self.events[i]
        return ret
