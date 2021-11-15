class label_ordine:
    def __init__(self, codice, nome, prezzo, label):
        self.codice = codice
        self.nome_categoria = nome
        self.label = label
        self.prezzo = prezzo

## Per ora mi servono solo label e nome_categoria
## Il prezzo e il codice non mi servono a un cazzo
    def get_nome(self):
        return self.nome_categoria

    def get_label(self):
        return self.label

    def get_prezzo(self):
        return self.prezzo