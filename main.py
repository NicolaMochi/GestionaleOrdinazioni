import sys
from PyQt5.QtWidgets import QApplication
from Login.view.loginInterface import loginInterface

if __name__=='__main__':
    app = QApplication(sys.argv)
    Login = loginInterface()
    Login.show()
    app.exec_()