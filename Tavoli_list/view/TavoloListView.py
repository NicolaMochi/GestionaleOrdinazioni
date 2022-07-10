from PySide2.QtWidgets import QPushButton, QFrame, QVBoxLayout, QLabel, QListWidgetItem, QWidget, QToolButton, QHBoxLayout
from Utilities.UIFunctions import UIFunctions


class TavoloListView:
    def __init__(self, home, lista_tavoli_controller, vista_ordine):
        self.row = 0
        self.column = 0
        self.home = home
        self.uifunctions = UIFunctions()
        self.lista_tavoli_controller = lista_tavoli_controller
        self.nuovo_item = None
        self.flag = False
        self.vista_ordine = vista_ordine

        self.tavolo_selected = None

        self.entrato = 0

    def add_tavolo_to_widget(self, tavolo_to_add):
        self.uifunctions.add_to_table(self.home.tableWidget_tavoli, tavolo_to_add, self.flag, 4, len(self.lista_tavoli_controller.get_lista()))

    def delete_tavolo(self):
        if len(self.lista_tavoli_controller.get_lista()) == 0:
            self.home.label_ordine_tavolo.setText("Devi prima aggiungere un nuovo Tavolo")
            self.home.label_ordine_tavolo.setStyleSheet("font: 9pt 'Poppins';")
            return
        self.uifunctions.remove_last_widget(self.home.tableWidget_tavoli, len(self.lista_tavoli_controller.get_lista()), 4)
        del self.lista_tavoli_controller.get_lista()[-1]
        self.lista_tavoli_controller.save_tavoli_list()
        print("Tavolo Eliminato")
    #print("C'è stato un errore, non riuscito a eliminare il tavolo")

    # Questa funzione non fa niente a livello di dati, solo front end
    def delete_ordine(self):
        try:
            item_clicked = self.home.tableWidget_tavoli.currentItem()
            self.tavolo_selected = self.lista_tavoli_controller.get_tavolo_by_index(int(item_clicked.text().split()[1]) - 1)
            if len(self.tavolo_selected.get_lista_ordini_tavolo())==0:
                self.home.label_ordine_tavolo.setText("Non ci sono ordini per questo tavolo")
                self.home.label_ordine_tavolo.setStyleSheet("font: 9pt 'Poppins';")
            else:
                self.home.lista_ordini_tavolo.clear()
                self.home.label_ordine_tavolo.setText("Ordini Cancellati correttamente")
                self.home.label_ordine_tavolo.setStyleSheet("font: 9pt 'Poppins';")
                self.tavolo_selected.get_lista_ordini_tavolo().clear()
                self.home.label_datetime_ordine_tavolo.setText("")
                self.home.btn_stampa_scontrino.setText("Totale: 0€")
                #self.FUNZIONE CHE ELIMINA GLI ORDINI DAL TAVOLO PER DAVVERO, SULLA LISTA

                self.lista_tavoli_controller.elimina_ordini_tavolo(self.tavolo_selected)

                self.lista_tavoli_controller.get_tavolo_by_index(self.tavolo_selected.get_codice_tavolo()).get_lista_ordini_tavolo().clear()
                self.lista_tavoli_controller.save_tavoli_list()

        except:
            self.home.label_ordine_tavolo.setStyleSheet("font: 9pt 'Poppins';")
            self.home.label_ordine_tavolo.setText("Devi prima aggiungere un nuovo Tavolo")



    def go_to_order(self):
        self.vista_ordine.view(self.tavolo_selected.get_codice_tavolo())
        print(self.tavolo_selected.get_codice_tavolo())

    def show_tavolo(self):
        self.home.lista_ordini_tavolo.clear()
        item_clicked = self.home.tableWidget_tavoli.currentItem()

        try:
            self.tavolo_selected = self.lista_tavoli_controller.get_tavolo_by_index(int(item_clicked.text().split()[1]) - 1)
            self.home.btn_add_ordine.clicked.connect(self.go_to_order)
        except:
            self.home.label_ordine_tavolo.setText("Per visualizzare un nuovo tavolo\n devi prima aggiungerlo")
            self.home.label_ordine_tavolo.setStyleSheet("font: 9pt 'Poppins';")
            return

        ordine_tavolo = 0
        self.home.label_ordine_tavolo.clear()
        self.home.label_ordine_tavolo.setText('')

        try:
            index = len(self.tavolo_selected.get_lista_ordini_tavolo()) - 1
            self.home.label_datetime_ordine_tavolo.setText(
            self.tavolo_selected.get_lista_ordini_tavolo()[index].get_data_ora_ordine())
            #self.home.btn_stampa_scontrino.clicked.connect(self.scontrino_tavolo)
        except:
            self.home.label_ordine_tavolo.setText("Non ci sono ordini per questo tavolo")
            self.home.label_ordine_tavolo.setStyleSheet("font: 9pt 'Poppins';")
            return


        if len(self.tavolo_selected.get_lista_ordini_tavolo()) != 0:
            self.home.lista_ordini_tavolo.clear()
            for ordine in self.tavolo_selected.get_lista_ordini_tavolo():
                label_text_ordine = QLabel()
                label_text_ordine.setObjectName(u"label")

                label_text_ordine.setText(
                    label_text_ordine.text() + "Ordine: " + str(ordine_tavolo) +
                    ordine.get_descrizione_ordine() + '\n')
                ordine_tavolo += 1
                self.add_order_to_list(label_text_ordine.text(), ordine)

            self.totale_tavolo =  str(self.lista_tavoli_controller.total_price_from_id(int(item_clicked.text().split()[1]) - 1))
            self.home.btn_stampa_scontrino.setText("Totale:  " + self.totale_tavolo + '€')
            self.home.btn_stampa_scontrino.clicked.connect(lambda: self.scontrino_tavolo())


    def add_order_to_list(self, text, ordine):

        widget = QWidget(self.home.lista_ordini_tavolo)
        button = QPushButton(widget)
        if(ordine.get_stato()==False):
            button.setText("Consegna")
            button.setStyleSheet(u"QPushButton{\n"
                                              "font: 400 9pt \"Poppins\";\n"
                                              "color: rgb(43, 43, 43);\n"
                                              "letter-spacing:0.2px ;\n"
                                              "margin-top:10px}\n"
                                              "QPushButton:hover{ \n"
                                              "	font: 400 10pt \"Poppins\"; cursor:pointer"
                                              "}")
        else:
            button.setText("Evaso")
            button.setStyleSheet(u"QPushButton{\n"
                                 "font: 400 9pt \"Poppins\";\n"
                                 "color: #aaa;\n"
                                 "letter-spacing:0.2px ;\n"
                                 "margin-top:10px}\n"
                                 "QPushButton:hover{ \n"
                                 "	font: 400 10pt \"Poppins\"; cursor:pointer"
                                 "}")
            button.setFlat(False)

        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        widget.setStyleSheet("background-color: transparent!important")
        item = QListWidgetItem(text)
        self.home.lista_ordini_tavolo.addItem(item)
        self.home.lista_ordini_tavolo.setItemWidget(item, widget)
        button.clicked.connect(lambda: self.change_order_state(button, ordine))


    def change_order_state(self, button, ordine):
        if (ordine.get_stato()==False):
                    ordine.set_stato(True)
                    button.setStyleSheet("font: 400 9pt \"Poppins\"; color: #aaa")
                    button.setText("Evaso")
        else:
                    ordine.set_stato(False)
                    button.setStyleSheet("font: 400 9pt \"Poppins\";\n"
                                          "color: rgb(43, 43, 43);\n")
                    button.setText("Consegna")
        self.lista_tavoli_controller.save_tavoli_list()



    def scontrino_tavolo(self):
        try:
            self.delete_ordine()
            self.home.label_ordine_tavolo.setText("Non ci sono ordini da pagare")
        except:
            self.home.label_ordine_tavolo.setText("Seleziona un tavolo per stampare il suo scontrino")

    def fill_list_tavoli_widget(self, lista_tavoli, flag):
        self.uifunctions.inizialize_ui_table(self.home.tableWidget_tavoli, 4, lista_tavoli, flag)
        self.home.tableWidget_tavoli.cellClicked.connect(self.show_tavolo)



