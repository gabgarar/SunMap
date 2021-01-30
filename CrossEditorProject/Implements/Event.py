class Event(object):

    def __init__(self, **kwargs):
        self.comm = kwargs['comm']

    def getCommand(self):
        return self.comm

    def getDescription(self):
        pass

    def parse(self, comm):
        return comm.lower() == self.comm

    def checkCommand(self, **kwargs):
        pass

    def execute(self, mmap, comm):
        pass
