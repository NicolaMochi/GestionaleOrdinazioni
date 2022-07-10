
class PortataController:
    def __init__(self, portata):
        self.portata = portata

    def __str__(self):
        return self.portata.nome

    def get_categoria(self):
        return self.portata.categoria
    def get_ingredienti(self):
        return self.portata.ingredienti
    def get_prezzo(self):
        return self.portata.prezzo
    def get_portata_id(self):
        return self.portata.piatto_id

    def set_categoria(self, categoria):
        self.portata.categoria = categoria

    def set_nome(self, nome):
        self.portata.nome = nome

    def set_prezzo(self, prezzo):
        self.portata.prezzo = prezzo

    def set_ingredienti(self, ingredienti):
        self.portata.ingredienti = ingredienti

    def stampa_ingredienti_portata(self):
        ingredienti_string = ''
        for i in self.portata.ingredienti:
            ingredienti_string = ingredienti_string + ' ' + i.get_ingrediente_nome()
        return ingredienti_string


