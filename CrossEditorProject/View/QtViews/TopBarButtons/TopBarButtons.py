from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHBoxLayout, QWidget


class TopBarButtons(QHBoxLayout):
    def __init__(self, PrincipalGrid, MainWindow):
        QHBoxLayout.__init__(self)

        self.setObjectName("horizontalLayout")

        # Button 6.
        self.pushButton_6 = QtWidgets.QPushButton(PrincipalGrid)
        self.pushButton_6.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignBottom)

        # Button 5.
        self.pushButton_5 = QtWidgets.QPushButton(PrincipalGrid)
        self.pushButton_5.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignBottom)

        # Button 4.
        self.pushButton_4 = QtWidgets.QPushButton(PrincipalGrid)
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignBottom)

        # Button 3.
        self.pushButton_3 = QtWidgets.QPushButton(PrincipalGrid)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignBottom)

        # Button 2.
        self.pushButton_2 = QtWidgets.QPushButton(PrincipalGrid)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignBottom)

        # Button 1.
        self.pushButton_1 = QtWidgets.QPushButton(PrincipalGrid)
        self.pushButton_1.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_1.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_1.setFlat(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.addWidget(self.pushButton_1, 0, QtCore.Qt.AlignBottom)

        self.retranslateUi(MainWindow)

    def setNav(self, bar):
        self.addWidget(bar)
        self.addWidget(QWidget())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_6.setText(_translate("MainWindow", "A"))
        self.pushButton_5.setText(_translate("MainWindow", "B"))
        self.pushButton_4.setText(_translate("MainWindow", "C"))
        self.pushButton_3.setText(_translate("MainWindow", "D"))
        self.pushButton_2.setText(_translate("MainWindow", "E"))
        self.pushButton_1.setText(_translate("MainWindow", "F"))
