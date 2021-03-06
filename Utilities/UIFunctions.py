from PySide2.QtCore import QPropertyAnimation
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QAbstractItemView, QTableWidgetItem


class UIFunctions():
    def __init__(self):
        self.row = 0
        self.column = 0
        self.utlima_tabella = None

    ##function to expand and collapse menu
    def toggleMenu(self, maxWidth, home, enable):
        if enable:

            width = home.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 0

            if width == 0:
                widthExtend = maxExtend
            else:
                widthExtend = standard

            self.animation = QPropertyAnimation(home.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.start()




    def inizialize_ui_table(self, nome_tabella, numero_colonne, lista_da_usare, flag):
        if len(lista_da_usare) / numero_colonne <= 1: nome_tabella.setColumnCount(len(lista_da_usare))
        elif len(lista_da_usare) == 0: nome_tabella.setColumnCount(1)
        else: nome_tabella.setColumnCount(numero_colonne)
        nome_tabella.setRowCount((len(lista_da_usare) / numero_colonne) + 1)
        nome_tabella.clear()
        nome_tabella.setEditTriggers(QAbstractItemView.NoEditTriggers)
        if flag or self.utlima_tabella != nome_tabella:
            self.row = 0
            self.column = 0
        for x in lista_da_usare:
            print("var x" + str(x))
            nuovo_item = QTableWidgetItem()
            nuovo_item.setFont(QFont("Poppins", 12, QFont.Medium))
            nuovo_item.setTextAlignment(Qt.AlignHCenter)
            nuovo_item.setText(x.__str__())
            nome_tabella.setItem(self.row, self.column, nuovo_item)
            self.column += 1
            if self.column % numero_colonne == 0:
                self.row += 1
                self.column = 0
        self.utlima_tabella = nome_tabella


    def add_to_table(self, tabella_da_usare, oggetto_da_aggiungere, flag, numero_colonne, length_lista):
        # Qui si pu?? agire meglio usando il RowCount
        if flag == True or ((length_lista-1)%numero_colonne==0): tabella_da_usare.setRowCount(tabella_da_usare.rowCount() + 1)
        riga = 0
        colonna = 0
        if (length_lista-1)<numero_colonne:
            tabella_da_usare.setColumnCount(length_lista)
            riga = 0
            colonna = tabella_da_usare.columnCount()-1 ## Il conteggio delle colonne parte da zero
        else:
            riga = int(length_lista/numero_colonne)
            colonna = int(length_lista % numero_colonne)-1 ## Il conteggio delle colonne parte da zero
        nuovo_item = QTableWidgetItem()
        nuovo_item.setText(oggetto_da_aggiungere.__str__())
        nuovo_item.setFont(QFont("Poppins", 12, QFont.Medium))
        nuovo_item.setTextAlignment(Qt.AlignHCenter)
        tabella_da_usare.setItem(riga, colonna, nuovo_item)

    def remove_last_widget(self, tabella_da_usare, length_lista, colonne):
        if length_lista<colonne:
            tabella_da_usare.item(tabella_da_usare.rowCount()-1, length_lista-1).setText("")
        elif (tabella_da_usare.rowCount()*tabella_da_usare.columnCount())%length_lista == 0:
            print("entrato nel primo if")
            tabella_da_usare.item(tabella_da_usare.rowCount()-1, tabella_da_usare.columnCount()-1).setText("")
        else:
            numero_riga = 0
            numero_colonna = 0
            i = 1
            diff = 0
            while i:
                if length_lista - i*tabella_da_usare.columnCount() > 0:
                    diff = length_lista - i*tabella_da_usare.columnCount()
                    numero_riga += 1
                    i+=1
                else:
                    i = 0
                    numero_colonna = diff-1
                    tabella_da_usare.item(numero_riga, numero_colonna).setText("")

        if (length_lista-1)%colonne==0: tabella_da_usare.setRowCount(length_lista/colonne)
        print("pipo")

    ## Questa funzione fa il check che i campi passati nella lista non siano vuoti
        # Se sono vuoti scrive il messaggio di errore sulla label passata
    def check(self, lista_campi, label_errore):
        for i in lista_campi:
            if i == "":
                label_errore.setText("Compila i campi")
                return True
        return False

    def fill_categorie_to_order(self, home, lista_da_usare):
        ## Determino la tabella di categorie che devo modificare
        self.table = None
        if home.Pages_widget.currentWidget() == home.OrdiniPage: self.table = home.table_categorie
        elif home.Pages_widget.currentWidget() == home.MenuPage: self.table = home.table_categorie_menu
        ## Aggiungo tutte le categorie nella tabella corretta
        column = 0
        self.table.clear()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setColumnCount(len(lista_da_usare)+1)
        for x in range(len(lista_da_usare)+1):
            nuovo_item = QTableWidgetItem()
            if x == 0: nuovo_item.setText("Vedi Tutti")
            else:
                nuovo_item.setText(lista_da_usare[x-1].__str__())
            font_nuovo_item = QFont("Dubai", 14, QFont.Medium)
            nuovo_item.setFont(font_nuovo_item)
            nuovo_item.setTextAlignment(Qt.AlignHCenter)
            self.table.setItem(0, column, nuovo_item)
            column += 1

    def check_prezzo_portata(self, gui, prezzo):
        if not prezzo.isnumeric():
            gui.lineEdit_prezzo.setText("Scrivi un numero")
            gui.lineEdit_prezzo.setStyleSheet(
                "font: 8pt 'Poppins';"
                "color: rgb(120, 120, 120);"
                "border: solid;"
                "border-bottom: 2px solid black;"
            )
            return True
        else: return False



