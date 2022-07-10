class Utilities:
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


    def start_posti(self):
        posti_totali = self.get_posti_totali()
        self.home.label_posti.setText(str(posti_totali) + '/' + str(posti_totali))

    def update_posti(self):
        posti_totali = self.get_posti_totali()
        posti_occupati = self.get_posti_occupati()
        self.home.label_posti.setText(str(posti_totali - posti_occupati) + '/' + str(posti_totali))




