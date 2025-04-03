from database.DB_connect import DBConnect
from model.corso import Course


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select c.codins
                   from iscritticorsi.corso c"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])
        cursor.close()
        cnx.close()
        #processa res

        return res

    @staticmethod
    def getAllCourses():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                   from iscritticorsi.corso c
                   """

        cursor.execute(query)

        res = []
        for row in cursor:
            # res.append(Corso(codins=row["codins"],
            #                  crediti=row["crediti"],
            #                  nome=row["nome"],
            #                  pd = row["pd"]))
            res.append(Course(**row))  #modo rapido per aggiungere
                                      # ogni valore del dizionario row
        cursor.close()
        cnx.close()
        #processa res

        return res

    @staticmethod
    def getCoursePD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                   from iscritticorsi.corso c
                   where c.pd = %s"""

        cursor.execute(query,(pd,))

        res = []
        for row in cursor:
            res.append(Course(**row))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def gestcoursesPDwithRegistered(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT c.codins, c.crediti, c.nome, c.pd, count(*) as n
                    from corso c, iscrizione i
                    where c.codins = i.codins
                    and c.pd = %s
                    group by c.codins, c.crediti, c.nome, c.pd"""

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append(
                (Course(row["codins"],row["crediti"],row["nome"],row["pd"]),row["n"])
            )

        cursor.close()
        cnx.close()
        return res

if __name__ == '__main__':
     for c in DAO.gestcoursesPDwithRegistered(1):
         print(c)