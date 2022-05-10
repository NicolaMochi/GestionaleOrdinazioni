################################################################################
##
'''
__author__: Dennis Pierantozzi
'''
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
from PySide2.QtWidgets import QApplication

# IMPORT FUNCTIONS
from Home.view.HomeView import HomeView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeView()
    window.show()
    sys.exit(app.exec_())