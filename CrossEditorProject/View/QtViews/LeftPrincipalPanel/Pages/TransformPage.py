from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QInputDialog


class TransformPage(QVBoxLayout):
    def __init__(self, PrincipalGrid, Ctrl, MainWindow):
        QVBoxLayout.__init__(self)

        self.ctrl = Ctrl
        self.principal = PrincipalGrid

        self.style = """
                     color: #000000;
                     font: 11pt "Arial";
        """

        numButtons = 3

        self.labels = ["Squricle transform", "Plate Carrée", "Synoptic Map"]
        for i in range(numButtons):
            self.setButton(i)
        self.addWidget(QtWidgets.QWidget())

    def setButton(self, i):
        pushButton = QtWidgets.QPushButton(self.principal)
        pushButton.setStyleSheet(self.style)
        pushButton.setMinimumSize(QtCore.QSize(200, 40))
        name = "pushButton_" + str(i)
        pushButton.setObjectName(name)
        pushButton.setText(self.labels[i])
        pushButton.clicked.connect(lambda: self.actions(pushButton))
        self.addWidget(pushButton, 0, QtCore.Qt.AlignBottom)

    def actions(self, label):
        print(label.text())

        comm = None
        # Lineal bright in percentile
        if str(label.text()) == self.labels[0]:
            comm = "polar"

        elif str(label.text()) == self.labels[1]:
            val = self.getDouble()
            if val is not None:
                comm = "plate " + str(val)

        elif str(label.text()) == self.labels[2]:
            comm = "synoptic " + str(13)

        if comm is not None:
            print(comm)
            self.ctrl.execute(comm=comm)

    def getDouble(self):
        str_i = "Value to fill between 2 days."
        i, okPressed = QInputDialog.getDouble(self.principal, str_i, "Value :", 2, 0, 100, 5)
        if okPressed:
            return i
        else:
            return None
