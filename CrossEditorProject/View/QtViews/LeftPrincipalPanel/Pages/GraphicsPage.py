from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QInputDialog


class GraphicsPage(QVBoxLayout):
    def __init__(self, PrincipalGrid, Ctrl, MainWindow):
        QVBoxLayout.__init__(self)

        self.ctrl = Ctrl
        self.principal = PrincipalGrid

        self.style = """
                     color: #000000;
                     font: 11pt "Arial";
        """

        numButtons = 2

        self.labels = ["Histogram", "Fourier"]
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
            comm = "hist"

        elif str(label.text()) == self.labels[1]:
            comm = "fft"

        if comm is not None:
            print(comm)
            self.ctrl.execute(comm=comm)
