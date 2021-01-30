'''
Load commands from a terminal
'''
from View.View import View


class Terminal(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        cont = True
        while cont:
            comm = input("Enter your command : ")
            self.ctrl.execute(comm=comm)

