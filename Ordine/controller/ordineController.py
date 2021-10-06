
class ordineController:
    def __init__(self, ordine):
        self.ordine = ordine()

    def get_codice_ordine(self):
        return self.ordine.get_codice_ordine()

    def get_stato(self):
        return self.ordine.get_stato()

    def get_prezzo_ordine(self):
        return self.ordine.get_prezzo_ordine()

    def get_descrizione_ordine(self):
        return self.ordine.get_descrizione_ordine()

    def get_data_ora_ordine(self):
        return self.ordine.get_data_ora_ordine()

    def get_tipo_ordine(self):
        return self.ordine.get_tipo_ordine()
