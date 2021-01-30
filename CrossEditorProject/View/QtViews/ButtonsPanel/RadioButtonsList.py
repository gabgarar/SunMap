from PyQt5.QtWidgets import QHBoxLayout
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from Implements.ViewEvents.Toppings import setAtt


class RadioButtonsList(QHBoxLayout):
    def __init__(self, PrincipalGrid, Ctrl, MainWindow):
        QHBoxLayout.__init__(self)
        self.setContentsMargins(20, 15, 20, 15)
        self.setSpacing(50)
        self.setObjectName("horizontalLayout_3")

        # self.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.addWidget(QtWidgets.QWidget())
        # Button 5.
        self.radioButton_5 = QtWidgets.QRadioButton(PrincipalGrid)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setAutoRepeat(False)
        self.radioButton_5.setAutoExclusive(False)
        self.radioButton_5.toggled.connect(lambda: self.contours(Ctrl))
        self.radioButton_5.setObjectName("radioButton_5")
        self.addWidget(self.radioButton_5, 0, QtCore.Qt.AlignHCenter)

        # Button 4.
        self.radioButton_4 = QtWidgets.QRadioButton(PrincipalGrid)
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setAutoRepeat(False)
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.toggled.connect(lambda: self.grid(Ctrl))
        self.radioButton_4.setObjectName("radioButton_4")
        self.addWidget(self.radioButton_4, 0, QtCore.Qt.AlignHCenter)

        # Button 3.
        self.radioButton_3 = QtWidgets.QRadioButton(PrincipalGrid)
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(lambda: self.showCromos(Ctrl))
        self.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignHCenter)

        # Button 2.
        self.radioButton_2 = QtWidgets.QRadioButton(PrincipalGrid)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda: self.showLimb(Ctrl))
        self.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignHCenter)

        # Button 1.
        self.radioButton_1 = QtWidgets.QRadioButton(PrincipalGrid)
        self.radioButton_1.setAutoExclusive(False)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.toggled.connect(lambda: self.hideAxis(Ctrl))
        self.addWidget(self.radioButton_1, 0, QtCore.Qt.AlignHCenter)

        self.addWidget(QtWidgets.QWidget())

        self.retranslateUi(MainWindow)

    def hideAxis(self, Ctrl):
        setAtt("hideAxis")
        Ctrl.execute(comm="update")

    def contours(self, Ctrl):
        setAtt("printContours")
        Ctrl.execute(comm="update")

    def showLimb(self, Ctrl):
        setAtt("printLimb")
        Ctrl.execute(comm="update")

    def showCromos(self, Ctrl):
        setAtt("printCromos")
        Ctrl.execute(comm="update")

    def grid(self, Ctrl):
        setAtt("printGrid")
        Ctrl.execute(comm="update")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.radioButton_5.setText(_translate("MainWindow", "Contours"))
        self.radioButton_4.setText(_translate("MainWindow", "Grid"))
        self.radioButton_3.setText(_translate("MainWindow", "Cromosphere"))
        self.radioButton_2.setText(_translate("MainWindow", "Limb"))
        self.radioButton_1.setText(_translate("MainWindow", "Hide Axis"))
