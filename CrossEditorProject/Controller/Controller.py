class Controller(object):

    def __init__(self, **kwargs):
        self.editor = kwargs['editor']
        self.mode = kwargs['mode']
        self.parser = kwargs['parser']

    def addObserver(self, o):
        self.editor.addObserver(o)

    def removeObserver(self, o):
        self.editor.removeObserver(o)

    def reboot(self):
        self.editor.reboot()
    '''
    def reboot:
        self.simulador.reinicia();


    def addObserver(ObservadorSimuladorTrafico o)
        self.simulador.addObservador(o)


    def removeObserver(ObservadorSimuladorTrafico o):
        self.simulador.removeObservador(o);
    '''

    def execute(self, **kwargs):
        print("EXEC: ", kwargs['comm'])
        ret = None
        if kwargs['comm'] is not None:
            if kwargs['comm'] == "update":
                self.editor.updateViewers(None)
            else:
                sep = self.formatInput(kwargs['comm'])
                ev = self.parser.parseEvent(sep.pop(0))
                if ev is not None:
                    self.editor.setEvent(ev)
                    ret = self.editor.execute(sep)
                else:
                    print("\tThere in not command {} ".format(kwargs['comm']))

        return ret

    def getFits(self):
        return self.editor.getFits()

    def sayHello(self):
        return "HII"

    @staticmethod
    def formatInput(command):
        lower = command.lower()
        split = command.split()
        return split
