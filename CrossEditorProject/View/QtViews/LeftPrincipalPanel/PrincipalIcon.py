from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
import os

class PrincipalIcon(QLabel):
    def __init__(self, PrincipalGrid):
        QLabel.__init__(self, PrincipalGrid)
        self.setMinimumSize(QtCore.QSize(300, 100))
        self.setMaximumSize(QtCore.QSize(300, 100))
        self.setStyleSheet("background-color: rgb(255,255,255);")
        self.setText("")
        self.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)),'icon.png')))
        self.setScaledContents(False)
        self.setIndent(0)
        self.setObjectName("label")
