class label_ordine:
    def __init__(self, nome, prezzo, label):
        self.nome_categoria = nome
        self.label = label
        self.prezzo = prezzo

    def get_nome(self):
        return self.nome_categoria

    def get_label(self):
        return self.label

    def get_prezzo(self):
        return self.prezzo