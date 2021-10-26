from Personale_list.model.personale_list import personale_list

class personale_list_controller:
    def __init__(self):
        self.lista =personale_list()

    def controllo_login(self, nome, password):
        for cred in self.lista.lista_personale:
            if nome == cred.nome and password == cred.password:
                return cred.codice
            else:
                return False

    def add_personale(self, personale):
        self.lista.add_credenziale(personale)