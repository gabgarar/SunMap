import threading

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class StatsTable(QTableWidget):
    def __init__(self, Ctrl, PrincipalGrid):
        QTableWidget.__init__(self, PrincipalGrid)

        self.ctrl = Ctrl
        Ctrl.addObserver(self)
        self.setStyleSheet('background-color: #323232; border: None; font: 10pt "Arial"; color: #e9e9e9;')
        self.setObjectName("tableStats")

    def updateViewer(self, fits, ret):
        th = threading.Thread(target=self.refresh(fits, ret))
        th.start()

    def refresh(self, fits, ret):
        comm = "stats"
        self.clear()
        self.setRowCount(0)
        st = fits.getStats()
        self.setColumnCount(2)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)

        ind = 0
        for elem in st:
            self.insertRow(ind)
            self.setItem(
                ind, 0, QTableWidgetItem(str(elem))
            )
            self.setItem(
                ind, 1, QTableWidgetItem(str(st[elem]))
            )
            ind += 1
