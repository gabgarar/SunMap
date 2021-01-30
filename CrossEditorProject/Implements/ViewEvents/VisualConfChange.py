from Implements.Event import Event
from Implements.ViewEvents.Toppings import setAtt, printVisualParams, getParams


class VisualConfChange(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Change a visual param: Change a visual param to apply."

    def execute(self, mmap, comm):
        if not comm:
            print(self.getDescription())
        else:
            key = comm.pop(0)
            setAtt(key)
            printVisualParams()

            return getParams()





