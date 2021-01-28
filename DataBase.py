import sqlite3


class DataBase:
    db_name = "CodTracker.db"

    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def insert_into_DB(self, user):
        sql = """Insert into Users values ('{dis_id}','{battle_name}', {id})""".format(dis_id=user.dis_id,
                                                                                       battle_name=user.wz_name,
                                                                                       id=user.id)
        self.cursor.execute(sql)
        self.connection.commit()

    def update_DB(self, user):
        sql = """Update users set battlename = '{battle_name}', battleid = {battle_id} where id = {id}""".format(
            battle_name=user.wz_name,
            battle_id=user.id,
            id=user.dis_id
        )
        self.cursor.execute(sql)
        self.connection.commit()

    def check_user(self, user):
        sql = """select id, battlename, battleid from users where id = {id}""".format(id=user.dis_id)
        self.cursor.execute(sql)
        users = self.cursor.fetchone()
        return users
