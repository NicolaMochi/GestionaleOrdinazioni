import json
import os

from Personale.controller.personale_controller import personale_controller
from Personale.model.personale_model import personale_model

class personale_list:
    def __init__(self):
        self.lista_personale = []

        with open('Personale_list/data/personale.json') as f:
            lista_credenziali = json.load(f)
        for credenziale in lista_credenziali:
            self.add_credenziale(personale_controller(personale_model(credenziale["nome"], credenziale["cognome"], credenziale["password"], credenziale["codice"], credenziale["ruolo"])))

    ## Manca il salvataggio

    def add_credenziale(self, personale):
        self.lista_personale.append(personale)