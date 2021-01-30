from Implements.ParserCommand import ParserCommand
from Implements.ViewEvents.ViewCromosEvent import ViewCromosEvent
from Implements.ViewEvents.ViewLimbEvent import ViewLimbEvent
from Implements.ViewEvents.ViewFFTEvent import ViewFFTEvent
from Implements.ViewEvents.ViewGradientEvent import ViewGradientEvent
from Implements.ViewEvents.ViewHistEvent import ViewHistEvent
from Implements.ViewEvents.ViewSelectiveEvent import ViewSelectiveEvent
from Implements.ViewEvents.ViewerSequenceEvent import ViewerSequenceEvent
from Implements.ViewEvents.VisualConfChange import VisualConfChange


class ViewParseEvents(ParserCommand):
    events = [
        ViewGradientEvent(comm="colormap"),
        ViewHistEvent(comm="hist"),
        ViewFFTEvent(comm="fft"),
        ViewSelectiveEvent(comm="selective"),
        ViewLimbEvent(comm="limb"),
        ViewCromosEvent(comm="cromos"),
        ViewerSequenceEvent(comm="show"),
        VisualConfChange(comm="param")
    ]

    def __init__(self, name="ViewParseEvents"):
        super().__init__(name=name)

