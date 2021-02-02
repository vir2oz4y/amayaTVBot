from Statistics import CodStatistic
from dataBase.DataBase import DataBase
from User import User
import sqlite3

class DiscordCommands:

    @staticmethod
    def reg(message):
        db = DataBase()

        def wrapper(discordMessage):
            user = User.userFromMessage(discordMessage)
            statusResponse = CodStatistic().getUserStatistics(user)

            if statusResponse != 404:
                try:
                    addToDB(user)
                    return "Пользователь добавлен"

                except sqlite3.IntegrityError:
                    changeIntoDB(user)
                    return "Пользователь изменен"

            else:
                return "Запись не добавлена\nНеверные данные аккаунта или профиль закрыт"

        def addToDB(user):
            db.addToBD(user)

        def changeIntoDB(user):
            db.changeIntoDB(user)

        return wrapper(message)



