from Implements.Event import Event


class RedoEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Redo : Redo the previous change"

    def execute(self, mmap, comm):
        if comm is not None:
            val = comm['unre'].redo()
            if val is not None:
                mmap.setMap(val)

