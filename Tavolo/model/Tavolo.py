from Cliente.model.cliente import cliente

class Tavolo:
    def __init__(self, codice_tavolo, posti):
        self.posti_tavolo = posti
        self.codice_tavolo = codice_tavolo
        self.ordini_tavolo = []
        self.cliente_tavolo = cliente()





