from PySide2.QtCore import QPropertyAnimation


class UIFunctions():

    ##function to expand and collapse menu
    def toggleMenu(self, maxWidth, home, enable):
        if enable:

            width = home.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 50

            if width == 50:
                widthExtend = maxExtend
            else:
                widthExtend = standard

            self.animation = QPropertyAnimation(home.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.start()