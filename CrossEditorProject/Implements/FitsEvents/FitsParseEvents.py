from Implements.FitsEvents.DownloadEvent import DownloadEvent
from Implements.FitsEvents.HeaderFitsEvent import HeaderFitsEvent
from Implements.FitsEvents.SaveEvent import SaveFITSEvent
from Implements.FitsEvents.StatsEvent import StatsEvent
from Implements.FitsEvents.LoadEvent import LoadFITSEvent
from Implements.ParserCommand import ParserCommand


class FitsParseEvents(ParserCommand):
    events = [
        LoadFITSEvent(comm="load"),
        SaveFITSEvent(comm="save"),
        StatsEvent(comm="stats"),
        DownloadEvent(comm="down"),
        HeaderFitsEvent(comm="header")
    ]

    def __init__(self, name="FitsParseEvents"):
        super().__init__(name=name)
