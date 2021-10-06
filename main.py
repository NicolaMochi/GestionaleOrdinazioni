################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
from PySide2.QtWidgets import QApplication

# IMPORT FUNCTIONS
from Home.view.home_view import home_view

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = home_view()
    window.show()
    sys.exit(app.exec_())