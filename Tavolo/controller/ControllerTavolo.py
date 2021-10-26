
class ControllerTavolo:
    def __init__(self, tavolo):
        self.tavolo = tavolo()

    ## GETTER ##
    # def get_nome(self):
    #     return self.tavolo.codice_tavolo
    def get_codice_tavolo(self):
        return self.tavolo.get_codice_tavolo()


    def get_lista_ordini_tavolo(self):
        return self.tavolo.get_lista_ordini_tavolo()

    def get_cliente_tavolo(self):
        return self.get_cliente_tavolo()

    ## SETTER ##
    def set_tavolo_numero(self, numero):
        self.tavolo.numeroTavolo = numero

    def set_tavolo_posti(self, posti):
        self.tavolo.posti = posti

    def add_ordine(self, ordine):
        self.tavolo.add_ordine(ordine)

    def total_price(self):
        self.tavolo.total_price()

