
from PyQt5.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    def __init__(self, MainWindow):
        QStatusBar.__init__(self, MainWindow)

        #TODO Añadir mas adelante.