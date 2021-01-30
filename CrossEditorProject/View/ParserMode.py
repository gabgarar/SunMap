from View.QtViews.Interface import Interface
from View.Terminal.Terminal import Terminal


def parserModeView(**kwargs):
    if kwargs['mode'] == "TERM":
        return Terminal(mode=kwargs['mode'], ctrl=kwargs['ctrl'])
    elif kwargs['mode'] == "VIEW":
        return Interface(mode=kwargs['mode'], ctrl=kwargs['ctrl'])
    else:
        return None
