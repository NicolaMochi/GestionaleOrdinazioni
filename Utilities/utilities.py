class utilities:
    def __init__(self, tavoli_list_controller, home):
        self.posti_totali = 0
        self.posti_occupati = 0
        self.lista_tavoli = tavoli_list_controller
        self.home = home
        self.codice_tavolo_selected = None

    def set_codice_tavolo_selected(self, codice_tavolo):
        self.codice_tavolo_selected = codice_tavolo

    def get_posti_occupati(self):
        posti_occupati = 0
        for x in self.lista_tavoli.get_lista():
            if len(x.get_lista_ordini_tavolo()) >= 1:
                posti_occupati+=int(x.get_posti_tavolo())
        return posti_occupati

    def get_posti_totali(self):
        posti_totali = 0
        for x in self.lista_tavoli.get_lista(): posti_totali += int(x.get_posti_tavolo())
        return posti_totali

    ## Tre casi:
        # all'avvio del programma: calcola il numero totale dei posti
        # quando aggiungo un nuovo ordine e aggiorno i posti occupati
        # quando aggiungo un nuovo tavolo e aggiorno il numero totale

    def start_posti(self):
        posti_totali = self.get_posti_totali()
        self.home.label_posti.setText(str(posti_totali) + '/' + str(posti_totali))

    # def update_posti_occupati(self):
    #     print("entrato")
    #     if len(self.lista_tavoli.get_tavolo_by_index(self.codice_tavolo_selected).get_lista_ordini_tavolo()) > 1:return
    #     print("passato if len")
    #     self.posti_totali = 0
    #     for x in self.lista_tavoli.get_lista(): self.posti_totali += int(x.get_posti_tavolo())
    #     posti_tavolo_selected = self.lista_tavoli.get_tavolo_by_index(self.codice_tavolo_selected).get_posti_tavolo()
    #     print("posti tavolo che ha ordinato: " + str(posti_tavolo_selected))
    #     self.posti_occupati += int(posti_tavolo_selected)
    #     print("posti occupati: " + str(self.posti_occupati))
    #     self.home.label_posti.setText(str(self.posti_totali - self.posti_occupati) + '/' + str(self.posti_totali))

    def update_posti(self):
        posti_totali = self.get_posti_totali()
        posti_occupati = self.get_posti_occupati()
        self.home.label_posti.setText(str(posti_totali - posti_occupati) + '/' + str(posti_totali))


    # def posti(self, codice_tavolo):
    #     self.posti_totali = 0
    #     for x in self.lista_tavoli.get_lista():
    #         print("Codice Tavolo: " + str(x.get_codice_tavolo()))
    #         #print("posti Tavolo: " + str(x.get_posti_tavolo() + '/n'))
    #         self.posti_totali += int(x.get_posti_tavolo())
    #     if codice_tavolo == -1:
    #     if codice_tavolo == -2:
    #         self.home.label_posti.setText(str(self.posti_totali - self.posti_occupati) + '/' + str(self.posti_totali))
    #     else:


    # def update_posti_rimanenti(self, home, ):
    #     print("Posti totali in update"+str(self.posti_totali))
    #     print("Posti tavolo selezionato: " + str(posti_tavolo_selected))




