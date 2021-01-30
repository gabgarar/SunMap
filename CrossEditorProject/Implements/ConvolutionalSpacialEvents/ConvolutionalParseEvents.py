from Implements.ConvolutionalSpacialEvents.SobelFilterEvent import SobelFilterEvent
from Implements.ConvolutionalSpacialEvents.StaticFilters import StaticFilters
from Implements.ParserCommand import ParserCommand


class ConvolutionalParseEvents(ParserCommand):
    events = [
        StaticFilters(comm="convu"),
        SobelFilterEvent(comm="sobel")
    ]

    def __init__(self, name="ConvolutionalParseEvents"):
        super().__init__(name=name)
