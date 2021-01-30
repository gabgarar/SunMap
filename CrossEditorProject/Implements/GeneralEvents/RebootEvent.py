from Implements.Event import Event


class RebootEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Reboot : Reboot the project"

    def execute(self, mmap, comm):
        if comm is not None:
           comm['fits'].reboot()
           comm['hist'].reboot()