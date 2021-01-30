from Implements.Composition.CompositionParseEvents import CompositionParseEvents
from Implements.ConvolutionalSpacialEvents.ConvolutionalParseEvents import ConvolutionalParseEvents
from Implements.FitsEvents.FitsParseEvents import FitsParseEvents
from Implements.FormatEvents.FormatParseEvent import FormatParseEvents
from Implements.GeneralEvents.GeneralParseEvents import GeneralParseEvents
from Implements.LinealSpacialEvents.LinealParserEvents import LinealParseEvents
from Implements.Parser import Parser
from Implements.ViewEvents.ViewParseEvents import ViewParseEvents


class ParseEvents(Parser):
    parsers = [
        LinealParseEvents(),
        ConvolutionalParseEvents(),
        FitsParseEvents(),
        FormatParseEvents(),
        GeneralParseEvents(),
        ViewParseEvents(),
        CompositionParseEvents()
    ]

    def __init__(self, name="PrincipalParser"):
        super().__init__(name=name)

    def help(self):
        hh = []
        for i in range(len(self.parsers)):
            hh.append(self.parsers[i].getHelp())
        # To show:
        for i in range(len(hh)):
            for key in hh[i]:
                print("{}".format(key))
                print("--------------------")
                for elem in hh[i][key]:
                    print("  *\t{}".format(elem))
                print("--------------------")
        return hh

    def isSpecialComm(self, comm):
        if comm and comm.lower() == "help":
            self.help()
            return True
        return False

    def parseEvent(self, comm):
        ret = None
        if not self.isSpecialComm(comm):
            for i in range(len(self.parsers)):
                event = self.parsers[i].hasCommand(comm)
                if event is not None:
                    ret = event
            return ret
