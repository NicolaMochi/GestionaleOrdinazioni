class portata:
    def __init__(self, piatto_id, nome, categoria, prezzo, ingredienti):
        self.piatto_id = piatto_id
        self.prezzo = prezzo
        self.categoria = categoria
        self.nome = nome
        # ingredienti dovrà essere una lista []
        self.ingredienti = ingredienti

    def get_nome_portata(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_prezzo(self):
        return self.prezzo

