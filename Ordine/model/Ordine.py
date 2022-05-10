class Ordine:
    def __init__(self, codice_ordine, stato, prezzo, descrizione, data_ora, tipo):
        self.codice_ordine = codice_ordine
        self.stato = stato
        self.prezzo_ordine = prezzo
        self.descrizione = descrizione
        self.modifiche_richieste = None
        self.data_ora_ordine = data_ora
        self.tipo = tipo #locale o da asporto
