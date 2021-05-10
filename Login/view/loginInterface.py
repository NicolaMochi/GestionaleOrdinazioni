from PyQt5.QtWidgets import QDialog
from Login.LoginDesign.login import Ui_Dialog

class loginInterface(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.login = Ui_Dialog()
        self.login.setupUi(self)
        self.show()