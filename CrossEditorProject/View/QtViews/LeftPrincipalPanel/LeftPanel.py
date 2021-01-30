from PyQt5.QtWidgets import QVBoxLayout

from View.QtViews.LeftPrincipalPanel.LeftMenu import LeftMenu
from View.QtViews.LeftPrincipalPanel.PrincipalIcon import PrincipalIcon


class LeftPanel(QVBoxLayout):  # Soy vertical layout
    def __init__(self, Ctrl, PrincipalGrid, MainWindow):
        QVBoxLayout.__init__(self)
        self.setObjectName("verticalLayout")

        # Icon Label.
        self.label = PrincipalIcon(PrincipalGrid)
        self.addWidget(self.label)

        # Left Menu.
        self.LeftMenu = LeftMenu(Ctrl, PrincipalGrid, MainWindow)
        self.LeftMenu.setStyleSheet("background-color: #323232;")
        self.addWidget(self.LeftMenu)
