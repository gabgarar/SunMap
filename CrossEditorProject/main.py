from Controller.Controller import Controller
from Implements.ParseEvents import ParseEvents
from Model.Editor import Editor
from View.ParserMode import parserModeView
import sys

if __name__ == "__main__":

#mode = "TERM"
	mode = str(sys.argv[1])
	#mode = "VIEW"
	print("Loading editor ...")
	editor = Editor()

	print("Loading parser events ...")
	parser = ParseEvents()

	print("Loading controller ...")
	ctrl = Controller(mode=mode, editor=editor, parser=parser)

	print("Loading view mode : {} ".format(mode))
	view = parserModeView(mode=mode, ctrl=ctrl)

	view.run()