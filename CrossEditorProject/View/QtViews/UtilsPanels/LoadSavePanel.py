from PyQt5.QtWidgets import QFileDialog, QDialog


class FileDialog(QDialog):
    def __init__(self, tt, Ctrl):
        QDialog.__init__(self)
        self.ctrl = Ctrl

        if tt == "Simple":
            self.comm = self.openFileNameDialog()
        elif tt == "Sequence":
            self.comm = self.openFileNamesDialog()
        elif tt == "Save":
            self.comm = self.saveFileDialog()
        else:
            raise NotImplementedError()

    def getComm(self):
        return self.comm

    # Individual File.
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Load an individual file.", "",
                                                  "FITS Files (*.fits)", options=options)
        if fileName:
            comm = "LOAD " + fileName
            print(comm)
            return comm
        else:
            return None

    # Multiple Files.
    def openFileNamesDialog(self):

        dir = QFileDialog.getExistingDirectory(self, "Select a multiple files")
        if dir:
            comm = "LOAD " + dir
            return comm
        else:
            return None

    # Save File.
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save the current file.", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            comm = "SAVE" + fileName
            return fileName
        else:
            return None

