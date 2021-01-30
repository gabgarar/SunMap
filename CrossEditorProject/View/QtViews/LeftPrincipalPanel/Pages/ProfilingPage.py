from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QInputDialog


class ProfilingPage(QVBoxLayout):
    def __init__(self, PrincipalGrid, Ctrl, MainWindow):
        QVBoxLayout.__init__(self)

        self.ctrl = Ctrl
        self.principal = PrincipalGrid

        self.style = """
                     color: #000000;
                     font: 11pt "Arial";
        """

        numButtons = 2

        self.labels = ["Gaussian smoothing", "Median smooth"]
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
            val = self.getDouble()
            if val is not None:
                comm = "blur gauss " + str(val)

        elif str(label.text()) == self.labels[1]:
            val = self.getDouble()
            if val is not None:
                comm = "blur median " + str(val)

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
