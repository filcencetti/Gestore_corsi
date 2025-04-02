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