import unittest

from Menu.controller.MenuController import MenuController
from Ordine.controller.OrdineController import OrdineController
from Ordine.model.Ordine import Ordine
from Personale.controller.PersonaleController import PersonaleController
from Personale.model.PersonaleModel import PersonaleModel
from Personale_list.controller.PersonaleListController import PersonaleListController
from Portata.controller.PortataController import PortataController
from Portata.model.PortataModel import PortataModel
from Tavoli_list.controller.TavoloListController import TavoloListController
from Tavolo.controller.ControllerTavolo import ControllerTavolo
from Tavolo.model.TavoloModel import TavoloModel

##################################
#       TEST DEL PROGRAMMA       #
##################################


class Test(unittest.TestCase):
    def setUp(self):
        self.portata_to_add = PortataController(PortataModel(100, "margherita", "pizza", "5", "mozzarella pomodoro"))
        self.menu = MenuController()

        self.ordine_to_add = OrdineController(Ordine(0, False, 22, "pizza \n margherita", "10/07/2022 00:39:29", "Locale"))
        self.tavoli_controller = TavoloListController()
        self.tavolo_to_add = ControllerTavolo(TavoloModel(0, 5))

        self.personale_to_add = PersonaleController(PersonaleModel("nome", "cognome", "123456", int(0), "Amministratore"))
        self.personale_controller = PersonaleListController()

    def test_inserisci_portata(self):
        self.assertIsNotNone(self.portata_to_add)
        self.menu.add_portata(self.portata_to_add)
        self.assertTrue(self.portata_to_add in self.menu.get_menu())

    def test_elimina_portata(self):
        self.assertIsNotNone(self.portata_to_add)
        self.menu.delete_portata(self.portata_to_add)
        self.assertFalse(self.portata_to_add in self.menu.get_menu())

    def test_update_portata(self):
        self.assertIsNotNone(self.portata_to_add)
        self.menu.add_portata(self.portata_to_add)
        self.portata_to_add.set_nome("margherita di bufala")
        self.menu.substitute_portata(0, self.portata_to_add)
        self.assertTrue(self.menu.get_menu()[0].__str__() == "margherita di bufala")

    def test_add_tavolo(self):
        self.assertIsNotNone(self.tavolo_to_add)
        self.tavoli_controller.add_tavolo(self.tavolo_to_add)
        self.assertTrue(self.tavolo_to_add in self.tavoli_controller.get_lista())

    def test_delete_tavolo(self):
        self.assertIsNotNone(self.tavolo_to_add)
        self.tavoli_controller.delete_tavolo(self.tavolo_to_add)
        self.assertFalse(self.tavolo_to_add in self.tavoli_controller.get_lista())

    def test_add_ordine_tavolo(self):
        self.assertIsNotNone(self.tavolo_to_add)
        self.assertIsNotNone(self.ordine_to_add)
        self.tavoli_controller.add_tavolo(self.tavolo_to_add)
        self.tavoli_controller.add_ordine_from_id(self.tavolo_to_add.get_codice_tavolo(), self.ordine_to_add)
        self.assertTrue(self.ordine_to_add in self.tavoli_controller.get_lista()[0].get_lista_ordini_tavolo())

    def test_delete_ordini_tavolo(self):
        self.tavoli_controller.add_tavolo(self.tavolo_to_add)
        self.tavoli_controller.add_ordine_from_id(self.tavolo_to_add.get_codice_tavolo(), self.ordine_to_add)
        self.tavoli_controller.get_lista()[self.tavolo_to_add.get_codice_tavolo()].clear_ordini_tavolo()
        self.assertFalse(self.ordine_to_add in self.tavoli_controller.get_lista()[self.tavolo_to_add.get_codice_tavolo()].get_lista_ordini_tavolo())

    def test_add_personale(self):
        self.assertIsNotNone(self.personale_to_add)
        self.personale_controller.add_personale(self.personale_to_add)
        self.assertTrue(self.personale_to_add in self.personale_controller.get_lista())

    def test_update_personale(self):
        self.personale_controller.add_personale(self.personale_to_add)
        self.personale_controller.modifica_utente(self.personale_to_add, ["", "nuovo cognome", "", "404"])
        self.assertTrue(self.personale_controller.find_user(["nome", "nuovo cognome"]).get_cognome_personale() == "nuovo cognome")

    def test_delete_personale(self):
        self.personale_controller.add_personale(self.personale_to_add)
        self.personale_controller.remove_personale(self.personale_to_add)
        self.assertFalse(self.personale_to_add in self.personale_controller.get_lista())

if __name__ == '__main__':
    unittest.main()
