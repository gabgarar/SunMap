import threading

from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem


class HeaderTable(QTableWidget):
    def __init__(self, Ctrl, PrincipalGrid):
        QTableWidget.__init__(self, PrincipalGrid)

        self.ctrl = Ctrl
        Ctrl.addObserver(self)
        self.setStyleSheet('background-color: #323232; border: None; font: 10pt "Arial"; color: #e9e9e9;')
        self.setObjectName("tableFITS")

    def updateViewer(self, fits, ret):
        th = threading.Thread(target=self.refresh(fits, ret))
        th.start()

    def refresh(self, fits, ret):
        st = fits.getCards()
        rows = len(st)
        self.setColumnCount(2)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)

        ind = 0
        for elem in st:
            self.insertRow(ind)
            for column_number, data in enumerate(elem):
                clear = str(data).strip().split('/')
                self.setItem(
                    ind, column_number, QTableWidgetItem(clear[0])
                )
            ind += 1
