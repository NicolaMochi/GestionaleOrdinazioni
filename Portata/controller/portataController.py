
class portataController:
    def __init__(self, portata):
        self.portata = portata

    ## GETTER ##
    # def get_nome(self):
    #     return self.tavolo.codice_tavolo
    def __str__(self):
        return self.portata.nome

    def get_categoria(self):
        return self.portata.categoria

    def get_ingredienti(self):
        return self.portata.ingredienti

    def get_prezzo(self):
        return self.portata.prezzo

    def get_piatto_id(self):
        return self.portata.piatto_id



