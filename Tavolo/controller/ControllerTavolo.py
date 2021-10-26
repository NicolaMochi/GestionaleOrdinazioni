
class ControllerTavolo:
    def __init__(self, tavolo):
        self.tavolo = tavolo

    ## GETTER ##
    # def get_nome(self):
    #     return self.tavolo.codice_tavolo
    def __str__(self):
        return 'Tavolo' + ' ' + str(self.tavolo.codice_tavolo + 1)

    def get_codice_tavolo(self):
        return self.tavolo.codice_tavolo

    def get_lista_ordini_tavolo(self):
        return self.tavolo.ordini_tavolo

    def get_cliente_tavolo(self):
        return self.tavolo.cliente_tavolo

    def get_posti_tavolo(self):
        return self.tavolo.posti_tavolo

    def add_ordine(self, ordine):
        self.tavolo.ordini_tavolo.append(ordine)

    def total_price(self):
        prezzo = 0
        for x in self.tavolo.ordini_tavolo:
            prezzo += x.get_prezzo_ordine()
        return prezzo

    ## SETTER ##
    def set_tavolo_numero(self, numero):
        self.tavolo.numeroTavolo = numero

    def set_tavolo_posti(self, posti):
        self.tavolo.posti = posti



