from Implements.FormatEvents.CastingEvent import CastingEvent
from Implements.FormatEvents.NormalizeEvent import NormalizeEvent
from Implements.FormatEvents.RescaleEvent import RescaleEvent
from Implements.ParserCommand import ParserCommand


class FormatParseEvents(ParserCommand):
    events = [
        NormalizeEvent(comm="normalize"),
        RescaleEvent(comm="rescale"),
        CastingEvent(comm="cast")
    ]

    def __init__(self, name="FormatParseEvents"):
        super().__init__(name=name)

