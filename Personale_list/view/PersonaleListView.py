from Personale.view.PersonaleView import PersonaleView
from Personale.view.gui_add_personale import gui_add_personale


class PersonaleListView:
    def __init__(self, home, personale_controller, uifunctions):
        self.row = 0
        self.column = 0
        self.home = home
        self.lista_personale = personale_controller
        self.nuovo_item = None
        self.personale_view = PersonaleView(home, personale_controller)
        self.uifunctions = uifunctions


    def view(self, codice_personale):
        self.home.Pages_widget.setCurrentWidget(self.home.PersonalePage)
        self.uifunctions.inizialize_ui_table(self.home.table_personale, 6, self.lista_personale.lista.lista_personale, True)
        if(codice_personale):
            self.home.table_personale.cellClicked.connect(self.personale_view.display_edit_item)
            self.home.add_nuovo_personale.clicked.connect(self.personale_view.display_new_personale)


