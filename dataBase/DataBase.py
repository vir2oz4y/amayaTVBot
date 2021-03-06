import sqlite3
from User import User

class DataBase:
    databaseName = 'amaya.db'

    def __init__(self):
        self.connection = sqlite3.connect(self.databaseName)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def createBD(self):
        sql = """CREATE TABLE users
                  (id int primary key, battleNetName text, tracker int)
               """
        self.cursor.execute(sql)

    def addToBD(self, user):
        sql = """insert into users values ({id}, '{battleNetName}', {tracker})""".format(id=user.id,
                                                                                         battleNetName=user.battleNetName,
                                                                                         tracker=user.tracker)
        self.cursor.execute(sql)
        self.connection.commit()

    def changeIntoDB(self, user):
        sql = """update users set battleNetName= '{battleNetName}',tracker={tracker} where id = {id}""".format(
                                                                                                        id=user.id,
                                                                                                        battleNetName=user.battleNetName,
                                                                                                        tracker=user.tracker)
        self.cursor.execute(sql)
        self.connection.commit()

    def getUser(self, userId):
        sql = """select * from users where id = {id}""".format(id=userId)
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        return user


if __name__ == '__main__':
    DB = DataBase()
