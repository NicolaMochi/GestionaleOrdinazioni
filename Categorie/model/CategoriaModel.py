class CategoriaModel:
    def __init__(self, nome, codice):
        self.nome = nome
        self.codice = codice

    def get_nome_categoria(self):
        return self.nome
    def get_codice_categoria(self):
        return self.codice

