# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTextStream, QFile
import os
from View.QtViews.ButtonsPanel.RadioButtonsList import RadioButtonsList
from View.QtViews.LeftPrincipalPanel.LeftPanel import LeftPanel
from View.QtViews.MenuBar.MenuBar import MenuBar
from View.QtViews.SolarPanel.SolarPanel import SolarPanel
from View.QtViews.StatusBar.StatusBar import StatusBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Ctrl):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1332, 712)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        file = r'CrossEditorProject\View\QtViews\style.qss'
        qss_file = open(file).read()
        MainWindow.setStyleSheet(qss_file)
        #window.setStyleSheet(qdarkgraystyle.load_stylesheet())


        self.PrincipalGrid = QtWidgets.QWidget(MainWindow)
        self.PrincipalGrid.setObjectName("PrincipalGrid")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.PrincipalGrid)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.addLayout(RadioButtonsList(self.PrincipalGrid, Ctrl, MainWindow), 5, 0, 1, 1) # TODO.TODO.TODO.
        #self.gridLayout_3.addWidget(QtWidgets.QWidget())

        self.solarP = SolarPanel(Ctrl, MainWindow)
        self.gridLayout_3.addWidget(self.solarP, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.verticalLayout = LeftPanel(Ctrl, self.PrincipalGrid, MainWindow)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)  ##
        MainWindow.setCentralWidget(self.PrincipalGrid)

        self.statusbar = StatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = MenuBar(MainWindow, Ctrl)
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def getCtrl(self):
        return self.ctrl

