from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenu


class HelpMenu(QMenu):

    def __init__(self, mainPanel, Ctrl):
        self.ctrl = Ctrl
        QMenu.__init__(self, '&About', mainPanel)

        # Project
        self.addAction('&About Cross Editor', self.infoCross,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_C)

        # Commands
        self.addAction('&About Commands', self.helpCommands,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_H)

        # About
        self.addAction('&Abo', self.about,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_A)

    def infoCross(self):
        raise NotImplementedError()

    def helpCommands(self):
        raise NotImplementedError()

    def about(self):
        raise NotImplementedError()
