import datetime

from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QAbstractItemView, QLabel, QCheckBox, QPushButton

#from Categorie_list.view.categorie_list_view import categorie_list_view
from Categorie_list.view.categorie_list_view import categorie_list_view
from Menu.view.menu_view import menu_view
from Ordine.controller.ordine_controller import ordine_controller
from Ordine.model.ordine import ordine
from Ordini_list.view.label_ordine import label_ordine
from Utilities.UIFunctions import UIFunctions


class nuovo_ordine_view:
    def __init__(self, lista_categorie, home, lista_ordini, lista_tavoli, menu):
        self.home = home
        self.lista_ordini = lista_ordini
        self.lista_tavoli = lista_tavoli
        self.lista_categorie = lista_categorie
        self.menu = menu

        self.lista_label_ordine = []
        self.conta_label = 0
        self.codice_ordine = 0
        self.prezzo_ordine = 0
        self.ultima_aggiunta = None
        self.codice_ordine = 0
        self.codice_label_ordine = 0
        self.btn_categorie_caricate = []

    ## Questa funzione può andare su utilities
    def check_categoria_portata_to_add(self, categoria):
        for x in self.lista_label_ordine:
            if x.get_nome() == categoria:
                return x
        return False

    def add_to_order(self):
        portata = self.menu.get_portata_from_name(self.home.tableWidget.currentItem().text())
        check = self.check_categoria_portata_to_add(portata.get_categoria())
        if check!=False:
                nome_label = check.get_label()
                nome_label.setText(nome_label.text() + '\n' + "    " + portata.__str__() + "             " + portata.get_prezzo() + '€')
                self.prezzo_ordine += float(portata.get_prezzo())
                self.ultima_aggiunta = check
        else:
            nuovo_nome_label = "label_ordini" + str(self.conta_label)
            self.conta_label += 1
            nuova_label = QLabel(self.home.scrollAreaWidgetContents_2)
            self.home.verticalLayout_22.addWidget(nuova_label)
            nuova_label.setObjectName(nuovo_nome_label)
            nuova_label.setStyleSheet(u"font: 500 13pt \"Dubai\";\n padding: 10px;")
            nuova_label.setTextFormat(Qt.AutoText)
            nuova_label.setAlignment(Qt.AlignLeft|Qt.AlignTop)

            nuova_label_ordine = label_ordine(self.codice_label_ordine, portata.get_categoria(), portata.get_prezzo(), nuova_label)
            self.codice_label_ordine += 1
            self.lista_label_ordine.append(nuova_label_ordine)

            nuova_label.setText(portata.get_categoria()+':')
            nuova_label.setText(nuova_label.text() + '\n' + "    " + portata.__str__() + "             " + portata.get_prezzo() + '€')
            self.prezzo_ordine += float(portata.get_prezzo())
            self.ultima_aggiunta = nuova_label_ordine


    def elimina_ultima_aggiunta(self):
        try:
            testo_da_modificare = self.ultima_aggiunta.get_label().text()
            print(testo_da_modificare)
            self.ultima_aggiunta.get_label().setText(testo_da_modificare[:testo_da_modificare.rfind('\n')])
            print("testo da modificare nuovo: " + testo_da_modificare[:testo_da_modificare.rfind('\n')])
            if self.ultima_aggiunta.get_label().text().count('\n') < 1:
                print("entrato nell'if")
                self.ultima_aggiunta.get_label().setText("")
                self.home.verticalLayout_22.removeWidget(self.ultima_aggiunta.get_label())
                appoggio = self.lista_label_ordine[self.ultima_aggiunta.codice - 1]
                self.lista_label_ordine.remove(self.ultima_aggiunta)
                self.ultima_aggiunta = appoggio
        except:
            label_elimina_exception = QLabel(self.home.scrollAreaWidgetContents_2)
            self.home.verticalLayout_22.addWidget(label_elimina_exception)
            label_elimina_exception.setStyleSheet(u"font: 500 13pt \"Dubai\";\n padding: 10px;")
            label_elimina_exception.setTextFormat(Qt.AutoText)
            label_elimina_exception.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            label_elimina_exception.setText("Non c'è nulla da eliminare")


    def testo_ordine_from_labels(self):
        testo_ordine = ''
        for x in self.lista_label_ordine:
            testo_ordine = testo_ordine + '\n' + x.get_label().text()
        return testo_ordine


    def invia_ordine(self):
        for i in reversed(range(self.home.verticalLayout_22.count())):
            self.home.verticalLayout_22.itemAt(i).widget().deleteLater()
        descrizione = self.testo_ordine_from_labels()
        self.lista_label_ordine.clear()
        prezzo = self.prezzo_ordine
        stato = "Inviato"
        tipo = "Locale"
        data_ora = datetime.datetime.now() .strftime("%d/%m/%Y %H:%M:%S")
        #tavolo_id = self.home.comboBox_seleziona_tavolo.currentIndex()
        nuovo_ordine = ordine_controller(ordine(self.codice_ordine, stato, prezzo, descrizione, data_ora, tipo))
        self.lista_tavoli.add_ordine_from_id(self.codice_tavolo_selected, nuovo_ordine)
        self.codice_ordine += 1
        self.prezzo_ordine = 0
        #TypeError: 'int' object is not callable
        #crea oggetto utility
        #utility.posti_rimanenti()
        print(descrizione)
        print(prezzo)
        print(data_ora)

## Si può mettere nella UIFunctions
    # def show_categorie_in_table(self):
    #     clicked = self.home.table_categorie.currentItem()
    #     if clicked.text() == "Vedi Tutti":
    #         self.menu_view.fill_table_to_order()
    #         return
    #
    #     categoria_selected = self.lista_categorie.get_categoria_from_text(clicked.text())
    #     nome_categoria = categoria_selected.get_nome_categoria()
    #     row = 0
    #     column = 0
    #     self.home.tableWidget.clear()
    #
    #     ## Visualizzo le portate della categoria cliccata sulla tabella
    #     for x in self.menu.get_menu():
    #         print(x.get_categoria())
    #         if x.get_categoria() == nome_categoria:
    #             nome_portata = x.__str__()
    #             nuovo_item = QTableWidgetItem()
    #             nuovo_item.setText(nome_portata)
    #             nuovo_item.setTextAlignment(Qt.AlignHCenter)
    #             nuovo_item.setFont(QFont("Poppins", 14, QFont.Medium))
    #             self.home.tableWidget.setItem(row, column, nuovo_item)
    #             column += 1
    #             if column % 5 == 0:
    #                 row += 1
    #                 column = 0


    def view(self, codice_tavolo):
        self.codice_tavolo_selected = codice_tavolo
        self.home.label_tavolo.setText("Aggiungi ordini al Tavolo " + str(self.codice_tavolo_selected+1))
        self.home.Pages_widget.setCurrentWidget(self.home.OrdiniPage)
        self.menu_view = menu_view(self.home, self.menu, self.lista_categorie)
        self.menu_view.fill_table_to_order()
        uifunctions = UIFunctions()
        uifunctions.fill_categorie_to_order(self.home, self.lista_categorie)
        #self.categorie_view.fill_categorie_to_order()
        self.home.table_categorie.cellClicked.connect(categorie_list_view().show_categorie_in_table(self.home, self.menu_view, self.lista_categorie, self.menu))






