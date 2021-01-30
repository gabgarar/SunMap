from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class PrincipalIcon(QLabel):
    def __init__(self, PrincipalGrid):
        QLabel.__init__(self, PrincipalGrid)
        self.setMinimumSize(QtCore.QSize(300, 100))
        self.setMaximumSize(QtCore.QSize(300, 100))
        self.setStyleSheet("background-color: rgb(255,255,255);")
        self.setText("")
        self.setPixmap(QtGui.QPixmap(r'..\Icons\CrossEditorProjectIcon.png'))
        self.setScaledContents(False)
        self.setIndent(0)
        self.setObjectName("label")
