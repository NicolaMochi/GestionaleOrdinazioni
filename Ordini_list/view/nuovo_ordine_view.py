import datetime

from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QAbstractItemView, QLabel, QCheckBox

from Ordine.model.ordine import ordine
from Ordini_list.view.label_ordine import label_ordine


class nuovo_ordine_view:
    def __init__(self, lista_categorie, utility, home, lista_ordini, lista_tavoli, menu):
        self.home = home
        self.lista_ordini = lista_ordini
        self.lista_tavoli = lista_tavoli
        self.lista_categorie = lista_categorie
        self.menu = menu
        self.utility = utility

        self.lista_label_ordine = []
        self.conta_label = 0
        self.codice_ordine = 0
        self.prezzo_ordine = 0
        self.ultima_aggiunta = None
        self.codice_ordine = 0
        self.checkBox_categorie_caricate = []


    #Ogni volta che si aggiunge una categoria, aggiungo un checkbox che la identifica
    #al click sul checkbox dovrebbero comparire i piatti di quella sola categoria
    #tramite la funzione fill_menu_from_categoria
    #non funziona
    #non ho trovato un modo per far partire una funzione al click del checkbox

    def check_categoria_portata_to_add(self, categoria):
        for x in range(len(self.lista_label_ordine)):
            if self.lista_label_ordine[x].get_nome() == categoria:
                return self.lista_label_ordine[x]
        return False


    def add_to_order(self):
        portata = self.menu.get_portata_from_name(self.home.tableWidget.currentItem().text())
        check = self.check_categoria_portata_to_add(portata.get_categoria())
        if check!=False:
                nome_label = check.get_label()
                nome_label.setText(nome_label.text() + '\n' + "    " + portata.get_nome_portata() + "             " + portata.get_prezzo() + '€')
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

            nuova_label_ordine = label_ordine(portata.get_categoria(), portata.get_prezzo(), nuova_label)
            self.lista_label_ordine.append(nuova_label_ordine)

            nuova_label.setText(portata.get_categoria()+':')
            nuova_label.setText(nuova_label.text() + '\n' + "    " + portata.get_nome_portata() + "             " + portata.get_prezzo() + '€')
            self.prezzo_ordine += float(portata.get_prezzo())
            self.ultima_aggiunta = nuova_label_ordine


    def elimina_ultima_aggiunta(self):
        try:
            testo_da_modificare = self.ultima_aggiunta.get_label().text()
            self.ultima_aggiunta.get_label().setText(testo_da_modificare[:testo_da_modificare.rfind('\n')])
            if self.ultima_aggiunta.get_label().text().count('\n') <= 1:
                self.ultima_aggiunta.get_label().setText("")
                self.home.verticalLayout_22.removeWidget(self.ultima_aggiunta.get_label())
                self.lista_label_ordine.remove(self.ultima_aggiunta)
        except:
            label_elimina_exception = QLabel(self.home.scrollAreaWidgetContents_2)
            self.home.verticalLayout_22.addWidget(label_elimina_exception)
            label_elimina_exception.setStyleSheet(u"font: 500 13pt \"Dubai\";\n padding: 10px;")
            label_elimina_exception.setTextFormat(Qt.AutoText)
            label_elimina_exception.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            label_elimina_exception.setText("Non c'è nulla da eliminare")


    def testo_ordine_from_labels(self):
        testo_ordine = ''
        for x in range(len(self.lista_label_ordine)):
            testo_ordine = testo_ordine + '\n' + self.lista_label_ordine[x].get_label().text()
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
        tavolo_id = self.home.comboBox_seleziona_tavolo.currentIndex()
        nuovo_ordine = ordine(self.codice_ordine, stato, prezzo, descrizione, data_ora, tipo)
        self.lista_tavoli.add_ordine_from_id(tavolo_id, nuovo_ordine)
        self.codice_ordine += 1

        #TypeError: 'int' object is not callable
        #self.utility.posti_rimanenti()
        print(descrizione)
        print(prezzo)
        print(data_ora)


    def fill_menu_to_order(self):
        for i in range(len(self.lista_tavoli.get_lista())):
            self.home.comboBox_seleziona_tavolo.addItem(
                "Tavolo" + ' ' + str(self.lista_tavoli.get_lista()[i].get_codice_tavolo() + 1))

        row = 0
        column = 0
        if len(self.menu.get_menu()) / 5 <= 1:
            self.home.tableWidget.setColumnCount(len(self.menu.get_menu()))
        else:
            self.home.tableWidget.setColumnCount(5)
        self.home.tableWidget.setRowCount((len(self.menu.get_menu()) / 5) + 1)
        font_nuovo_item = QFont("Dubai", 14, QFont.Medium)

        self.home.tableWidget.clear()
        self.home.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for x in range(len(self.menu.get_menu())):
           nome_portata = self.menu.get_menu()[x].get_nome_portata()
           nuovo_item = QTableWidgetItem()
           nuovo_item.setText(nome_portata)
           nuovo_item.setTextAlignment(Qt.AlignHCenter)
           nuovo_item.setFont(font_nuovo_item)
           self.home.tableWidget.setItem(row, column, nuovo_item)
           column += 1
           if column % 5 == 0:
              row += 1
              column = 0


    def fill_categorie_to_order(self):
        #Questo if è sbagliato
        #Devo fare: if le due liste (checkBox caricate e lista_categorie.get_lista sono uguali o meno)
        if len(self.checkBox_categorie_caricate) == 0:
            for x in range(len(self.lista_categorie.get_lista())):
                nome_categoria = self.lista_categorie.get_lista()[x].get_nome_categoria()
                nuovo_checkBox = QCheckBox(self.home.frame_seleziona_categoria)
                self.checkBox_categorie_caricate.append(nuovo_checkBox)
                self.home.horizontalLayout_8.addWidget(nuovo_checkBox, 0, Qt.AlignHCenter)
                nuovo_checkBox.setText(QCoreApplication.translate("MainWindow", nome_categoria, None))
                nuovo_checkBox.setStyleSheet(
                    "QCheckBox {spacing: 5px;border: 2px solid white;padding:"
                    "4px;border-radius: 10px;background-color: rgb(255, 85, 0);font: 500 12pt 'Dubai';}"
                    "QCheckBox::indicator {width: 13px;height: 13px;}"
                    "QCheckBox::indicator:unchecked {background-color: white;}"            
                    "QCheckBox::indicator:unchecked:hover {background-color: black;}"
                    "QCheckBox::indicator:unchecked:pressed {background-color: green;}")
               ## if nuovo_checkBox.isChecked(): self.prova()
        else:
            numero_categorie_caricate = len(self.checkBox_categorie_caricate)
            numero_categorie_totali = len(self.lista_categorie.get_lista())
            x = numero_categorie_totali-numero_categorie_caricate
            while x<numero_categorie_totali:
                nome_categoria = self.lista_categorie.get_lista()[x].get_nome_categoria()
                #self.categorie_caricate.append(self.lista_categorie.get_lista()[x])
                nuovo_checkBox = QCheckBox(self.home.frame_seleziona_categoria)
                self.checkBox_categorie_caricate.append(nuovo_checkBox)
                self.home.horizontalLayout_8.addWidget(nuovo_checkBox, 0, Qt.AlignHCenter)
                nuovo_checkBox.setText(QCoreApplication.translate("MainWindow", nome_categoria, None))
                nuovo_checkBox.setStyleSheet(
                    "QCheckBox {spacing: 5px;border: 2px solid white;padding:"
                    "4px;border-radius: 10px;background-color: rgb(255, 85, 0);font: 500 12pt 'Dubai';}"
                    "QCheckBox::indicator {width: 13px;height: 13px;}"
                    "QCheckBox::indicator:unchecked {background-color: white;}"
                    "QCheckBox::indicator:unchecked:hover {background-color: black;}"
                    "QCheckBox::indicator:unchecked:pressed {background-color: green;}")
               ## nuovo_checkBox.clicked(self.prova)
                x += 1

    def view(self):
        self.home.Pages_widget.setCurrentWidget(self.home.OrdiniPage)
        self.fill_menu_to_order()
        #self.fill_categorie_to_order()





