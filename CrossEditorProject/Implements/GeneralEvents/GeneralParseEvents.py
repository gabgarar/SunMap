from Implements.GeneralEvents.ExitEvent import ExitEvent
from Implements.GeneralEvents.RebootEvent import RebootEvent
from Implements.GeneralEvents.RedoEvent import RedoEvent
from Implements.GeneralEvents.UndoEvent import UndoEvent
from Implements.ParserCommand import ParserCommand


class GeneralParseEvents(ParserCommand):
    events = [
        ExitEvent(comm="exit"),
        UndoEvent(comm="undo"),
        RedoEvent(comm="redo"),
        RebootEvent(comm="reboot")
    ]

    def __init__(self, name="GeneralParseEvents"):
        super().__init__(name=name)

