from Implements.Event import Event


class UndoEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Undo : Undo the previous change"

    def execute(self, mmap, comm):
        if comm is not None:
            val = comm['unre'].undo()
            if val is not None:
                print("HOLA ESTOY EN UNDO")
                mmap.setMap(val)
