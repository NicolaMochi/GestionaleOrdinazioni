from PyQt5.QtWidgets import QDialog, QMainWindow

from Home.HomeDesign.home import Ui_Home
from Login.LoginDesign.loginGui import Login_Gui


class loginInterface(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.login = Login_Gui()
        self.login.setupUi(self)
        self.homegui = Ui_Home()
        self.show()

        self.login.EnterButton.clicked.connect(self.clickto)

    def clickto(self):
        self.homegui.setupUi(self)
        self.show()


