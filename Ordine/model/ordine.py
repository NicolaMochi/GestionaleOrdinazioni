class ordine:
    def __init__(self, codice_ordine, stato, prezzo, descrizione, data_ora, tipo):
        self.codice_ordine = codice_ordine
        self.stato = stato
        self.prezzo_ordine = prezzo
        self.descrizione = descrizione
        self.modifiche_richieste = None
        self.data_ora_ordine = data_ora
        self.tipo = tipo #locale o da asporto

    def get_codice_ordine(self):
        return self.codice_ordine

    def get_stato(self):
        return self.stato

    def get_prezzo_ordine(self):
        return self.prezzo_ordine

    def get_descrizione_ordine(self):
        return self.descrizione

    def get_data_ora_ordine(self):
        return self.data_ora_ordine

    def get_tipo_ordine(self):
        return self.tipo