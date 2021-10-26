from PySide2.QtCore import QPropertyAnimation
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QAbstractItemView, QTableWidgetItem


class UIFunctions():
    def __init__(self):
        self.row = 0
        self.column = 0

    ##function to expand and collapse menu
    # def toggleMenu(self, maxWidth, home, enable):
    #     if enable:
    #
    #         width = home.frame_left_menu.width()
    #         maxExtend = maxWidth
    #         standard = 50
    #
    #         if width == 50:
    #             widthExtend = maxExtend
    #         else:
    #             widthExtend = standard
    #
    #         self.animation = QPropertyAnimation(home.frame_left_menu, b"minimumWidth")
    #         self.animation.setDuration(400)
    #         self.animation.setStartValue(width)
    #         self.animation.setEndValue(widthExtend)
    #         self.animation.start()


    ## Faccio le funzioni per:
        #riempire la tabella da zero con o senza il flag dato un numero di colonne
        #inserire un nuovo widget in una data tabella passato il testo

    def inizialize_ui_table(self, nome_tabella, numero_colonne, lista_da_usare, flag):
        if len(lista_da_usare) / numero_colonne <= 1: nome_tabella.setColumnCount(len(lista_da_usare))
        elif len(lista_da_usare) == 0: nome_tabella.setColumnCount(1)
        else: nome_tabella.setColumnCount(numero_colonne)
        nome_tabella.setRowCount((len(lista_da_usare) / numero_colonne) + 1)
        nome_tabella.clear()
        nome_tabella.setEditTriggers(QAbstractItemView.NoEditTriggers)
        if flag:
            self.row = 0
            self.column = 0
        for x in lista_da_usare:
            nuovo_item = QTableWidgetItem()
            nuovo_item.setFont(QFont("Poppins", 14, QFont.Medium))
            nuovo_item.setTextAlignment(Qt.AlignHCenter)
            nuovo_item.setText(x.__str__())
            nome_tabella.setItem(self.row, self.column, nuovo_item)
            self.column += 1
            if self.column % 3 == 0:
                self.row += 1
                self.column = 0

    def add_to_widget(self, tabella_da_usare, oggetto_da_aggiungere, flag):
        if flag == True: tabella_da_usare.setRowCount(tabella_da_usare.rowCount()+1)
        nuovo_item = QTableWidgetItem()
        nuovo_item.setText(oggetto_da_aggiungere.__str__())
        nuovo_item.setFont(QFont("Poppins", 14, QFont.Medium))
        nuovo_item.setTextAlignment(Qt.AlignHCenter)
        tabella_da_usare.setItem(self.row, self.column, nuovo_item)
        nuovo_item = None
        self.column += 1
        if self.column % 3 == 0:
            self.row += 1
            self.flag = True
            self.column = 0
