import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore Corsi edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements

        self.dd_PD = None
        self.dd_Codins = None
        self.btn_PrintCoursesPD = None
        self.btn_Print_RegisteredCoursesPD = None
        self.btn_Print_RegisteredCoursesPD = None
        self.btn_Print_CDSCodins = None
        self.lvTxtOut = None

    def load_interface(self):

        self.dd_PD = ft.Dropdown(label="Periodo Didattico",
                                 options=[ft.dropdown.Option("I"),
                                          ft.dropdown.Option("II")],
                                 width=300)

        self.dd_Codins = ft.Dropdown(label="Corso",width=300,on_change=self._controller.ddCodinsSelected)
        self._controller.fillddCodins()

        self.btn_PrintCoursesPD = ft.ElevatedButton(text="Stampa corsi",
                                                    on_click=self._controller.handlePrintCoursesPD,
                                                    width=300)
        self.btn_Print_RegisteredCoursesPD = ft.ElevatedButton(text="Stampa numero iscritti",
                                                    on_click=self._controller.handlePrintRegisteredCoursesPD,
                                                    width=300)
        self.btn_Print_RegisteredCodins = ft.ElevatedButton(text="Stampa iscritti al corso",
                                                    on_click=self._controller.handlePrintRegisteredCodins,
                                                    width=300)
        self.btn_Print_CDSCodins = ft.ElevatedButton(text="Stampa corsi",
                                                    on_click=self._controller.handlePrintCDSCodins,
                                                    width=300)
        self.lvTxtOut = ft.ListView(expand=True)


        row1 = ft.Row([self.dd_PD, self.btn_PrintCoursesPD, self.btn_Print_RegisteredCoursesPD,],alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self.dd_Codins, self.btn_Print_RegisteredCodins,self.btn_Print_CDSCodins,],alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(ft.Text(self._page.title),row1,row2,self.lvTxtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
