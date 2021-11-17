from Utilities.UIFunctions import UIFunctions


class tavolo_list_view:
    def __init__(self, home, lista_tavoli_controller, vista_ordine):
        self.row = 0
        self.column = 0
        self.home = home
        self.uifunctions = UIFunctions()
        self.lista_tavoli_controller = lista_tavoli_controller
        self.nuovo_item = None
        self.flag = False
        self.vista_ordine = vista_ordine

    def add_tavolo_to_widget(self, tavolo_to_add):
        self.uifunctions.add_to_table(self.home.tableWidget_tavoli, tavolo_to_add, self.flag, 4, len(self.lista_tavoli_controller.get_lista()))
        # if self.flag == True: self.home.tableWidget_tavoli.setRowCount(self.home.tableWidget_tavoli.rowCount()+1)
        # self.nuovo_item = QTableWidgetItem()
        # self.nuovo_item.setText('Tavolo' + ' ' + str(tavolo_to_add))
        # self.nuovo_item.setFont(QFont("Poppins", 14, QFont.Medium))
        # self.nuovo_item.setTextAlignment(Qt.AlignHCenter)
        # self.home.tableWidget_tavoli.setItem(self.row, self.column, self.nuovo_item)
        # self.nuovo_item = None
        # self.column += 1
        # if self.column % 3 == 0:
        #     self.row += 1
        #     self.flag = True
        #     self.column = 0

    def delete_tavolo(self):
        if len(self.lista_tavoli_controller.get_lista()) == 0:
            self.home.label_ordine_tavolo.setText("Devi prima aggiungere un nuovo Tavolo")
            return
        self.uifunctions.remove_last_widget(self.home.tableWidget_tavoli, len(self.lista_tavoli_controller.get_lista()), 4)
        del self.lista_tavoli_controller.get_lista()[-1]
        print("Tavolo Eliminato")
    #print("C'è stato un errore, non riuscito a eliminare il tavolo")


    def delete_ordine(self):
        try:
            item_clicked = self.home.tableWidget_tavoli.currentItem()
            tavolo = self.lista_tavoli_controller.get_tavolo_by_index(int(item_clicked.text().split()[1]) - 1)
            if len(tavolo.get_lista_ordini_tavolo())==0:
                self.home.label_ordine_tavolo.setText("Non ci sono ordini per questo tavolo")
            else:
                self.home.label_ordine_tavolo.setText("Ordini Cancellati correttamente")
                tavolo.get_lista_ordini_tavolo().clear()
                self.home.label_datetime_ordine_tavolo.setText("")
                self.home.btn_stampa_scontrino.setText("Totale: 0€")
        except:
            self.home.label_ordine_tavolo.setText("Devi prima aggiungere un nuovo Tavolo")


    def go_to_order(self):
        self.vista_ordine.view(self.tavolo_selected.get_codice_tavolo())
        print(self.tavolo_selected.get_codice_tavolo())

    def show_tavolo(self):
        item_clicked = self.home.tableWidget_tavoli.currentItem()
        try:
            self.tavolo_selected = self.lista_tavoli_controller.get_tavolo_by_index(int(item_clicked.text().split()[1]) - 1)
            self.home.btn_add_ordine.clicked.connect(self.go_to_order)
        except:
            self.home.label_ordine_tavolo.setText("Per visualizzare un nuovo tavolo\n devi prima aggiungerlo")
            return
        ordine_tavolo = 0
        self.home.label_ordine_tavolo.clear()
        self.home.label_ordine_tavolo.setText('')
        for ordine in self.tavolo_selected.get_lista_ordini_tavolo():
            self.home.label_ordine_tavolo.setText(
                self.home.label_ordine_tavolo.text() + "Ordine: " + str(ordine_tavolo) +
                ordine.get_descrizione_ordine() + '\n\n')
            ordine_tavolo += 1
        try:
            index = len(self.tavolo_selected.get_lista_ordini_tavolo()) - 1
            self.home.label_datetime_ordine_tavolo.setText(
                self.tavolo_selected.get_lista_ordini_tavolo()[index].get_data_ora_ordine())
        except:
            self.home.label_ordine_tavolo.setText("Non ci sono ordini per questo tavolo")

        self.home.btn_stampa_scontrino.setText("Totale:  " + str(self.lista_tavoli_controller.total_price_from_id(int(item_clicked.text().split()[1]) - 1)) + '€')



        #codice_tavolo_clicked = item_clicked.text().split()[1]
        #QUI DEVI FARE UN TRY EXCEPT PERCHE ITEM_CLICKED NON HA TEXT SE E' VUOTO!!
    #try
    #excepty
        #self.home.label_ordine_tavolo.setText("Devi prima aggiungere un nuovo Tavolo")


    def fill_list_tavoli_widget(self, lista_tavoli, flag):
        # self.home.tableWidget_tavoli.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # for x in lista_tavoli:
        #     print(x.get_codice_tavolo())
        # self.home.tableWidget_tavoli.setColumnCount(3)
        # if len(lista_tavoli) == 0 : self.home.tableWidget_tavoli.setRowCount(0)
        # elif len(lista_tavoli) <= 3 : self.home.tableWidget_tavoli.setRowCount(1)
        # elif len(lista_tavoli) / 3 == 0: self.home.tableWidget_tavoli.setRowCount(len(lista_tavoli) / 3)
        # else: self.home.tableWidget_tavoli.setRowCount((len(lista_tavoli) / 3) + 1)
        # font_nuovo_item = QFont("Poppins", 14, QFont.Medium)
        self.uifunctions.inizialize_ui_table(self.home.tableWidget_tavoli, 4, lista_tavoli, flag)
        # if flag:
        #     self.row = 0
        #     self.column = 0
        # for tavolo in lista_tavoli:
        #     nuovo_item = QTableWidgetItem()
        #     nuovo_item.setFont(font_nuovo_item)
        #     nuovo_item.setTextAlignment(Qt.AlignHCenter)
        #     nuovo_item.setText('Tavolo' + ' ' + str(tavolo.get_codice_tavolo()+1))
        #     self.home.tableWidget_tavoli.setItem(self.row, self.column, nuovo_item)
        #     self.column += 1
        #     if self.column % 3 == 0:
        #         self.row += 1
        #         self.column = 0
        self.home.tableWidget_tavoli.cellClicked.connect(self.show_tavolo)


