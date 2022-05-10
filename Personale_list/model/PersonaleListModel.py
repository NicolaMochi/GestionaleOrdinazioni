import json
import os

from Personale.controller.PersonaleController import PersonaleController
from Personale.model.PersonaleModel import PersonaleModel

class PersonaleListModel:
    def __init__(self):
        self.lista_personale = []

        with open('Personale_list/data/personale.json') as f:
            lista_credenziali = json.load(f)
        for credenziale in lista_credenziali:
            self.add_credenziale(PersonaleController(PersonaleModel(credenziale["nome"], credenziale["cognome"], credenziale["password"], credenziale["codice"], credenziale["ruolo"])))

    ## Manca il salvataggio

    def add_credenziale(self, personale):
        self.lista_personale.append(personale)