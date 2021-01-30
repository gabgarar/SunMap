from PyQt5.QtWidgets import QToolBox, QScrollArea, QListView
from PyQt5 import QtWidgets, QtCore

from View.QtViews.LeftPrincipalPanel.Pages.GraphicsPage import GraphicsPage
from View.QtViews.LeftPrincipalPanel.Pages.ContrastPage import ContrastPage
from View.QtViews.LeftPrincipalPanel.Pages.EqualizationPage import EqualizationPage
from View.QtViews.LeftPrincipalPanel.Pages.HeaderCardsPage import HeaderTable
from View.QtViews.LeftPrincipalPanel.Pages.ProfilingPage import ProfilingPage
from View.QtViews.LeftPrincipalPanel.Pages.StatsPage import StatsTable
from View.QtViews.LeftPrincipalPanel.Pages.TransformPage import TransformPage


class LeftMenu(QToolBox):
    def __init__(self, Ctrl, PrincipalGrid, MainWindow):
        QToolBox.__init__(self, PrincipalGrid)

        # Size Policy.

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(300, 0))
        self.setMaximumSize(QtCore.QSize(300, 16777215))
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setLineWidth(5)
        self.setObjectName("LeftMenu")

        styleSheet = """
                background-color: #323232;
                
                    """

        # P1.
        self.P1 = QtWidgets.QWidget()
        self.P1.setStyleSheet('background-color: #323232;')
        self.P1.setLayout(ContrastPage(PrincipalGrid, Ctrl, MainWindow))
        self.P1.setObjectName("P1")
        self.addItem(self.P1, "")

        # P2.
        self.P2 = QtWidgets.QWidget()
        self.P2.setStyleSheet('background-color: #323232;')
        self.P2.setLayout(EqualizationPage(PrincipalGrid, Ctrl, MainWindow))
        self.P2.setObjectName("P2")
        self.addItem(self.P2, "")

        # P3.
        self.P3 = QtWidgets.QWidget()
        self.P3.setStyleSheet('background-color: #323232;')
        self.P3.setLayout(ProfilingPage(PrincipalGrid, Ctrl, MainWindow))
        self.P3.setObjectName("P3")
        self.addItem(self.P3, "")

        # P4.
        self.P4 = QtWidgets.QWidget()
        self.P4.setStyleSheet('background-color: #323232;')
        self.P4.setLayout(TransformPage(PrincipalGrid, Ctrl, MainWindow))
        self.P4.setObjectName("P4")
        self.addItem(self.P4, "")

        # P5.
        self.P5 = QtWidgets.QWidget()
        self.P5.setStyleSheet('background-color: #323232;')
        self.P5.setLayout(GraphicsPage(PrincipalGrid, Ctrl, MainWindow))
        self.P5.setObjectName("P5")
        self.addItem(self.P5, "")

        # P6.
        self.P6 = StatsTable(Ctrl, PrincipalGrid)
        self.P6.setObjectName("P6")
        self.addItem(self.P6, "")

        # P7.
        self.P7 = HeaderTable(Ctrl, PrincipalGrid)
        self.P7.setObjectName("P7")
        self.addItem(self.P7, "")

        self.setCurrentIndex(6)
        self.layout().setSpacing(5)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setItemText(self.indexOf(self.P1), _translate("MainWindow", "contrast"))
        self.setItemText(self.indexOf(self.P2), _translate("MainWindow", "equalization"))
        self.setItemText(self.indexOf(self.P3), _translate("MainWindow", "profiling"))
        self.setItemText(self.indexOf(self.P4), _translate("MainWindow", "transforms"))
        self.setItemText(self.indexOf(self.P5), _translate("MainWindow", "graphics"))
        self.setItemText(self.indexOf(self.P6), _translate("MainWindow", "statistics"))
        self.setItemText(self.indexOf(self.P7), _translate("MainWindow", "header cards"))