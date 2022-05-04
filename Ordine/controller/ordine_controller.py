
class ordine_controller:
    def __init__(self, ordine):
        self.ordine = ordine

    def get_codice_ordine(self):
        return self.ordine.codice_ordine

    def get_stato(self):
        return self.ordine.stato

    def get_prezzo_ordine(self):
        return self.ordine.prezzo_ordine

    def get_descrizione_ordine(self):
        return self.ordine.descrizione

    def get_data_ora_ordine(self):
        return self.ordine.data_ora_ordine

    def get_tipo_ordine(self):
        return self.ordine.tipo

    def set_stato(self, stato):
        self.ordine.stato = stato
