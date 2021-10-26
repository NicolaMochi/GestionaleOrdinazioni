from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QTableWidget, QAbstractItemView


class tavolo_list_view:
    def __init__(self, home, tavoli_controller, uifunctions):
        self.row = 0
        self.column = 0
        self.home = home
        self.uifunctions = uifunctions
        self.tavoli_controller = tavoli_controller
        self.nuovo_item = None
        self.flag = False

    def add_tavolo_to_widget(self, tavolo_to_add):
        if self.flag == True: self.home.tableWidget_tavoli.setRowCount(self.home.tableWidget_tavoli.rowCount()+1)
        self.nuovo_item = QTableWidgetItem()
        self.nuovo_item.setText('Tavolo' + ' ' + str(tavolo_to_add))
        font_nuovo_item = QFont("Dubai", 14, QFont.Medium)
        self.nuovo_item.setFont(font_nuovo_item)
        self.nuovo_item.setTextAlignment(Qt.AlignHCenter)
        self.home.tableWidget_tavoli.setItem(self.row, self.column, self.nuovo_item)
        self.nuovo_item = None
        self.column += 1
        if self.column % 3 == 0:
            self.row += 1
            self.flag = True
            self.column = 0

    def delete_ordine(self):
        try:
            item_clicked = self.home.tableWidget_tavoli.currentItem()
            tavolo = self.tavoli_controller.get_tavolo_by_index(int(item_clicked.text().split()[1]) - 1)
            if len(tavolo.get_lista_ordini_tavolo())==0:
                self.home.label_ordine_tavolo.setText("Non ci sono ordini per questo tavolo")
            else:
                self.home.label_ordine_tavolo.setText("Ordini Cancellati correttamente")
                tavolo.get_lista_ordini_tavolo().clear()
                self.home.label_datetime_ordine_tavolo.setText("")
                self.home.btn_stampa_scontrino.setText("Totale: 0€")
        except:
            self.home.label_ordine_tavolo.setText("Devi prima aggiungere un nuovo Tavolo")

    def show_tavolo(self):
       # try:
            item_clicked = self.home.tableWidget_tavoli.currentItem()
            print(item_clicked.text())
            tavolo = self.tavoli_controller.get_tavolo_by_index(int(item_clicked.text().split()[1]) - 1)
            ordine_tavolo = 0
            self.home.label_ordine_tavolo.clear()
            self.home.label_ordine_tavolo.setText('')
            for ordine in tavolo.get_lista_ordini_tavolo():
                self.home.label_ordine_tavolo.setText(
                    self.home.label_ordine_tavolo.text() + "Ordine: " + str(ordine_tavolo) +
                    ordine.get_descrizione_ordine() + '\n\n')
                ordine_tavolo += 1
           # try:
                index = len(tavolo.get_lista_ordini_tavolo()) - 1
                self.home.label_datetime_ordine_tavolo.setText(
                    tavolo.get_lista_ordini_tavolo()[index].get_data_ora_ordine())
           # except:
                #self.home.label_ordine_tavolo.setText("Devi prima aggiungere un ordine")

            self.home.btn_stampa_scontrino.setText("Totale:  " + str(self.tavoli_controller.total_price_from_id(int(item_clicked.text().split()[1]) - 1)) + '€')
        #except:
            #self.home.label_ordine_tavolo.setText("Devi prima aggiungere un nuovo Tavolo")



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
        font_nuovo_item = QFont("Poppins", 14, QFont.Medium)
        self.uifunctions.inizialize_ui_table(self.home.tableWidget_tavoli, 3, lista_tavoli, flag)
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


