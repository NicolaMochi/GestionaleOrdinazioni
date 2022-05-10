from PySide2.QtWidgets import QDialog

from Personale.view.PersonaleView import PersonaleView


class PersonaleListView:
    def __init__(self, home, personale_controller, add_personale_view, uifunctions):
        self.row = 0
        self.column = 0
        self.home = home
        self.lista_personale = personale_controller
        self.nuovo_item = None
        self.personale_view = PersonaleView(home, personale_controller)
        self.uifunctions = uifunctions


    def view(self):
        self.home.Pages_widget.setCurrentWidget(self.home.PersonalePage)
        self.uifunctions.inizialize_ui_table(self.home.table_personale, 6, self.lista_personale.lista.lista_personale, True)
        self.home.table_personale.cellClicked.connect(self.personale_view.display_edit_item)
        self.home.add_nuovo_personale.clicked.connect(self.personale_view.display_new_personale)


