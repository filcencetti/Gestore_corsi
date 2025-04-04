import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue = None

    def fillddCodins(self):
        # for code in self._model.getCodins():
        #     self._view.dd_Codins.options.append(ft.dropdown.Option(code))
        for c in self._model.getAllCourses():
            self._view.dd_Codins.options.append(ft.dropdown.Option(key=c.codins,
                                                                   data=c,
                                                                   on_click = self._choiceDDCodins))

    def handlePrintCoursesPD(self,e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.dd_PD.value
        if pd is None:
            #self._view.lvTxtOut.controls.append(ft.Text(value="Attenzione! selezionare un periodo didattico!",color="red"))
            #self._view.update_pade()
            self._view.create_alert("Attenzione! selezionare un periodo didattico!")
            return

        if pd == "I":
            pdInt = 1
        else: pdInt = 2
        coursePD = self._model.getCoursesPD(pdInt)

        if len(coursePD) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun corso trovato in questo periodo."))
            self._view.update_page()
            return

        self._view.controls.append(ft.Text(f"Corsi del {pd} periodo didattico"))
        for c in coursePD:
            self._view.lvTxtOut.controls.append(ft.Text(c))
        self._view.update_page()

    def handlePrintRegisteredCoursesPD(self,e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.dd_PD.value
        if pd is None:
            self._view.create_alert("Seleziona il periodo didattico!")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        coursesPDwR = self._model.getcoursespdwithregisterd(pdInt)
        if len(coursesPDwR) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun corso trovato in questo periodo."))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Dettagli corsi del {pd} periodo didattico"))
        for c in coursesPDwR:
            self._view.lvTxtOut.controls.append(ft.Text(f"{c[0]} - N iscritti {c[1]}"))
        self._view.update_page()

    def handlePrintRegisteredCodins(self,e):
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Seleziona un corso!")
            return

        students = self._model.getstudentscourse(self._ddCodinsValue.codins)
        if len(students) == 0:
            self._view.lvTxtOut.controls.append(
                ft.Text("Nessuno studente iscritto a questo corso."))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append(
            ft.Text(f"Studenti iscritti al corso {self._ddCodinsValue}"))

        for s in students:
            self._view.lvTxtOut.controls.append(ft.Text(s)) # s ha un __str__
        self._view.update_page()


    def handlePrintCDSCodins(self,e):
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Seleziona un corso!")
            return
        cds = self._model.getCDSofCourse(self._ddCodinsValue.codins)
        if len(cds) == 0:
            self._view.lvTxtOut.controls.append(
                ft.Text("Nessuno CDS offre questo corso."))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append(
            ft.Text(f"Studenti iscritti al corso {self._ddCodinsValue}"))

        for c in cds:
            self._view.lvTxtOut.controls.append(ft.Text(f"CDS: {c[0]} - N iscritti: {c[1]}"))  # s ha un __str__
        self._view.update_page()



    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)
        print("In _choiceDDCodins", type(self._ddCodinsValue))

    def ddCodinsSelected(self, e):
        print("In ddCodinsSelected", type(self._view.dd_Codins.value))