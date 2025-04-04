from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCourses(self):
        return DAO.getAllCourses()

    def getCoursesPD(selfself,pd):
        return DAO.getCoursePD(pd)

    def getcoursespdwithregisterd(self,pd):
        return DAO.gestcoursesPDwithRegistered(pd)

    def getstudentscourse(self,codins):
     students = DAO.getStudentsCourse(codins)
     students.sort(key=lambda s: s.cognome)
     return students

    def getCDSofCourse(self,codins):
        cds = DAO.getCDSofCourse(codins)
        cds.sort(key=lambda c: c[1],reverse=True)
        return cds