class portata:
    def __init__(self, piatto_id, nome, categoria, prezzo, ingredienti):
        self.piatto_id = piatto_id
        self.prezzo = prezzo
        self.categoria = categoria
        self.nome = nome
        # ingredienti dovrà essere una lista []
        self.ingredienti = ingredienti

    def __str__(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_prezzo(self):
        return self.prezzo

    def get_piatto_id(self):
        return self.piatto_id

