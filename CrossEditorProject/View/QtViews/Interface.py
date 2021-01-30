from View.View import View
from PyQt5.QtWidgets import QApplication, QMainWindow
import qdarkgraystyle

from PyQt5 import QtCore
from View.QtViews.BASE import Ui_MainWindow
import os

class Interface(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        app = QApplication([])
        app.setStyle('Fusion')
        window = QMainWindow()
        main_window = Ui_MainWindow()
        main_window.setupUi(window, self.ctrl)
        window.show()

        app.exec_()


