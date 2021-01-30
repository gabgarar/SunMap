from Implements.LinealSpacialEvents.BinaryImageEvent import BinaryImageEvent
from Implements.LinealSpacialEvents.BlurEvent import BlurEvent
from Implements.LinealSpacialEvents.CentralLevelEvent import SigmodBrightEvent
from Implements.LinealSpacialEvents.ExtractBackgroundEvent import ExtractBackgroundEvent
from Implements.LinealSpacialEvents.HistEqualizationEvent import HistEqualizationEvent
from Implements.LinealSpacialEvents.LinealBrightEvent import LinealBrightEvent
from Implements.LinealSpacialEvents.PercentileBrightEvent import PercentileBrightEvent
from Implements.LinealSpacialEvents.PrincipalContourEvent import PrincipalContourEvent
from Implements.ParserCommand import ParserCommand


class LinealParseEvents(ParserCommand):
    events = [
        LinealBrightEvent(comm="bright"),
        HistEqualizationEvent(comm="equ"),
        BlurEvent(comm="blur"),
        PercentileBrightEvent(comm="perc"),
        BinaryImageEvent(comm="binary"),
        PrincipalContourEvent(comm="principal"),
        SigmodBrightEvent(comm="sigmod"),
        ExtractBackgroundEvent(comm="extract")

    ]

    def __init__(self, name="LinealParseEvents"):
        super().__init__(name=name)
