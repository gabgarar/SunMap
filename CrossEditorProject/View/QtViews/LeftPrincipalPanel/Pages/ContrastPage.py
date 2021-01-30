from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QInputDialog


class ContrastPage(QVBoxLayout):
    def __init__(self, PrincipalGrid, Ctrl, MainWindow):
        QVBoxLayout.__init__(self)

        self.ctrl = Ctrl
        self.principal = PrincipalGrid

        self.style = """
                     color: #000000;
                     font: 11pt "Arial";
        """

        numButtons = 5

        self.labels = ["Lineal bright", "Gamma adjust",
                       "Logarithm adjust", "Filtering regional",
                       "Filled regional"]
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
            val = self.getPercent()
            if val is not None:
                comm = "bright lineal " + str(val)

        # Gamma adjust
        elif str(label.text()) == self.labels[1]:
            val = self.getDouble()
            if val is not None:
                comm = "bright gamma " + str(val)

        # Logarithm adjust
        elif str(label.text()) == self.labels[2]:
            val = self.getDouble()
            if val is not None:
                comm = "bright log " + str(val)

        # Filtering Regional
        elif str(label.text()) == self.labels[3]:
            val = self.getDouble()
            if val is not None:
                comm = "bright regional " + str(val)

        # Filled Regional
        elif str(label.text()) == self.labels[4]:
            val = self.getDouble()
            if val is not None:
                comm = "bright filled " + str(val)

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
        i, okPressed = QInputDialog.getDouble(self.principal, str_i, "Value :", 2, 0, 100, 5)
        if okPressed:
            return i
        else:
            return None

    def getPercent(self):
        str_i = "Percentage of brightness that you want to increase or decrease:"
        i, okPressed = QInputDialog.getDouble(self.principal, str_i, "Value :", 20, -100, 100, 3)
        if okPressed:
            return i
        else:
            return None

    def getValue(self, val, min, max):
        str_i = "Enter a value for the Gaussian adjustment"
        i, okPressed = QInputDialog.getInt(self.principal, str_i, "Value :", 30, 0, 100, 10)
        if okPressed:
            return i
        else:
            return None
