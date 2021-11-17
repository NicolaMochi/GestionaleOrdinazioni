from Personale_list.model.personale_list import personale_list

class personale_list_controller:
    def __init__(self):
        self.lista = personale_list()

    # Manca il salvataggio

    def controllo_login(self, nome, password):
        for cred in self.lista.lista_personale:
            if nome == cred.get_nome_personale() and password == cred.get_password_personale():
                return cred.get_codice_personale()
            else:
                return False

    def add_personale(self, personale):
        self.lista.add_credenziale(personale)

    def get_lista(self):
        return self.lista.lista_personale

    def remove_personale(self, personale):
        self.lista.lista_personale.remove(personale)

    def find_user(self, credenziali):
        nome = credenziali[0]
        cognome = credenziali[1]
        for cred in self.lista.lista_personale:
            if nome == cred.get_nome_personale() and cognome == cred.get_cognome_personale():
                return cred

    def modifica_utente(self, user, nuove_credenziali):
        if user.get_nome_personale() != nuove_credenziali[0]: user.set_nome_personale(nuove_credenziali[0])
        if user.get_cognome_personale != nuove_credenziali[1]: user.set_cognome_personale(nuove_credenziali[1])
        if nuove_credenziali[2] != "": user.set_password_personale(nuove_credenziali[2])
        ruolo_attuale = user.get_ruolo_personale()
        if int(nuove_credenziali[3]) != user.get_codice_personale():
            user.set_codice_personale(int(nuove_credenziali[3]))
            if nuove_credenziali[3] == True:
                user.set_ruolo_personale("Amministr.")
            else: user.set_ruolo_personale("Dipendente")




