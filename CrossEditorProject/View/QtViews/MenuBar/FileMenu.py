from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu, QMessageBox, QInputDialog
from View.QtViews.UtilsPanels.LoadSavePanel import FileDialog


class FileMenu(QMenu):
    def __init__(self, MainWindow, Ctrl):
        self.mainPanel = MainWindow
        self.ctrl = Ctrl
        QMenu.__init__(self, '&File', self.mainPanel)

        # Load
        self.addAction('&Load Image', self.fileLoad,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_L)
        self.addAction('&Load Sequence', self.sequenceLoad,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_W)

        # Save
        self.addAction('&Save', self.fileSave,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.addAction('&Save as gif', self.fileSaveGif,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_G)
        # self.menuBar().addMenu(self.file_menu)

        # Exit
        self.addAction('&Exit', self.fileQuit,
                       QtCore.Qt.CTRL + QtCore.Qt.Key_L)

    def getMenu(self):
        return self

    # Load

    def fileLoad(self):
        self.ctrl.execute(comm=FileDialog("Simple", self.ctrl).getComm())

    def sequenceLoad(self):
        self.ctrl.execute(comm=FileDialog("Sequence", self.ctrl).getComm())

    # Save

    def fileSave(self):
        self.ctrl.execute(comm=FileDialog("Save").getComm())

    def fileSaveGif(self):
        self.ctrl.execute(comm="gif " + str(self.getDouble()))

    def getDouble(self):
        str_i = "Value"
        i, okPressed = QInputDialog.getDouble(self, "Get ms between images", "Value :", 250, 0, 100000, 0)
        if okPressed:
            return i
        else:
            return None

    # Exit

    def fileQuit(self):
        msgBox = QMessageBox(self)
        reply = msgBox.question(
            self, 'Warning',
            ('Do you want to exit the application?'),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.mainPanel.close()
