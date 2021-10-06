from Personale_credenziali_list.model.personale_list import personale_list

class personale_list_controller:
    def __init__(self):
        self.lista =personale_list()

    def controllo_login(self, username, password):
        for cred in self.lista.lista_personale:
            if username == cred.utente and password == cred.password:
                return cred.codice
            else:
                return 0