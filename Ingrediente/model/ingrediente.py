class ingrediente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def get_ingrediente_id(self):
        return self.id

    def get_ingrediente_nome(self):
        return self.nome