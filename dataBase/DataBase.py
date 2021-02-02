import sqlite3

class DataBase:
    databaseName = 'amaya.db'

    def __init__(self):
        self.connection = sqlite3.connect(self.databaseName)
        self.cursor = self.connection.cursor()

    def createBD(self):
        sql = """CREATE TABLE users
                  (id int, battleNetName text, tracker int)
               """
        self.cursor.execute(sql)


if __name__ == '__main__':
    DB = DataBase()