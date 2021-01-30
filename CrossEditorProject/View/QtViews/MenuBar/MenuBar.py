# Menu
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenuBar

from View.QtViews.MenuBar.FileMenu import FileMenu
from View.QtViews.MenuBar.HelpMenu import HelpMenu


class MenuBar(QMenuBar):

    def __init__(self, MainWindow, Ctrl):
        QMenuBar.__init__(self, MainWindow)

        self.setGeometry(QtCore.QRect(0, 0, 1332, 21))

        self.addMenu(FileMenu(MainWindow, Ctrl))
        #self.addMenu(HelpMenu(MainWindow, Ctrl))
