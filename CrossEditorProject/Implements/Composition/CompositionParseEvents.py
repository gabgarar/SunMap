from Implements.Composition.GifEvent import GifEvent
from Implements.Composition.PolarTransformEvent import TransformEvent
from Implements.Composition.SynopticEvent import SynopticEvent
from Implements.Composition.SynopticPlateEvent import SynopticPlateEvent
from Implements.ParserCommand import ParserCommand


class CompositionParseEvents(ParserCommand):
    events = [
        TransformEvent(comm="polar"),
        GifEvent(comm="gif"),
        SynopticEvent(comm="synoptic"),
        SynopticPlateEvent(comm="plate")
    ]

    def __init__(self, name="CompositionParseEvents"):
        super().__init__(name=name)
