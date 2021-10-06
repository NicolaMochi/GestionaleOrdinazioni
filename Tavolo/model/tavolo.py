from Cliente.model.cliente import cliente

class tavolo:
    def __init__(self, codice_tavolo, posti):
        self.posti_tavolo = posti
        self.codice_tavolo = codice_tavolo
        self.ordini_tavolo = []
        self.cliente_tavolo = cliente()

    def get_codice_tavolo(self):
        return self.codice_tavolo

    def get_lista_ordini_tavolo(self):
        return self.ordini_tavolo

    def get_cliente_tavolo(self):
        return self.cliente_tavolo

    def get_posti_tavolo(self):
        return self.posti_tavolo

    def add_ordine(self, ordine):
        self.ordini_tavolo.append(ordine)

    def total_price(self):
        prezzo = 0
        for x in range(len(self.ordini_tavolo)):
            prezzo += self.ordini_tavolo[x].get_prezzo_ordine()
        return prezzo
