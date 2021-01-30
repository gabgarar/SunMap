from Implements.Event import Event
import sys


class ExitEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Exit : Exit the program"

    def execute(self, mmap, comm):
        sys.exit(0)
