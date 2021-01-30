from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QInputDialog, QMessageBox


class EqualizationPage(QVBoxLayout):
    def __init__(self, PrincipalGrid, Ctrl, MainWindow):
        QVBoxLayout.__init__(self)

        self.ctrl = Ctrl
        self.principal = PrincipalGrid

        self.style = """
                     color: #000000;
                     font: 11pt "Arial";
        """

        numButtons = 4

        self.labels = ["Contrast stretching", "Global Equalization", "Adaptive equalization", "Rank equalization"]
        for i in range(numButtons):
            self.setButton(i)
        self.addWidget(QtWidgets.QWidget())

    def setButton(self, i):
        pushButton = QtWidgets.QPushButton(self.principal)
        pushButton.setStyleSheet(self.style)
        pushButton.setIconSize(QSize(20, 20))
        pushButton.setMinimumSize(QtCore.QSize(200, 40))
        name = "pushButton_" + str(i)
        pushButton.setObjectName(name)
        pushButton.setText(self.labels[i])
        pushButton.clicked.connect(lambda: self.actions(pushButton))
        #pushButton.setIcon(QIcon(QPixmap('../View/QtViews/Icons/bright.png')))
        self.addWidget(pushButton, 0, QtCore.Qt.AlignBottom)

    def actions(self, label):
        print(label.text())

        comm = None
        if str(label.text()) == self.labels[0]:
            val = self.getPercentile()
            if val is not None:
                comm = "equ contrast " + str(val)

        elif str(label.text()) == self.labels[1]:
            comm = "equ global"

        elif str(label.text()) == self.labels[2]:
            val = self.getDouble()
            if val is not None:
                comm = "equ adapt " + str(val)

        elif str(label.text()) == self.labels[3]:
            val = self.getValue(30, 0, 100)
            if val is not None:
                comm = "equ rank " + str(val)

        if comm is not None:
            print(comm)
            self.ctrl.execute(comm=comm)

    def getPercentile(self):
        i, okPressed = QInputDialog.getDouble(self.principal, "Percentile", "Percentile :", 98, 0, 100, 10)
        if okPressed:
            return i
        else:
            return None

    def getDouble(self):
        str_i = "Value"
        i, okPressed = QInputDialog.getDouble(self.principal, str_i, "Value :", 0.03, 0, 1, 10)
        if okPressed:
            return i
        else:
            return None

    def getValue(self, val, min, max):
        str_i = "Value"
        i, okPressed = QInputDialog.getInt(self.principal, str_i, "Value :", 30, 0, 100, 10)
        if okPressed:
            return i
        else:
            return None
