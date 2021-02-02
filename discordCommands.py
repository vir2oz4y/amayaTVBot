from Statistics import CodStatistic
from dataBase.DataBase import DataBase
from User import User
import sqlite3

class DiscordCommands:

    @staticmethod
    def registration(message):
        db = DataBase()

        def wrapper(discordMessage):  # главная функция
            user = User.userFromMessage(discordMessage)  # получили юсера из сообщения
            statusResponse = CodStatistic().getUserStatistics(user)  # проверили есть ли такой аккаунт

            if statusResponse != 404:  # если ответ получен
                try:
                    addToDB(user)  # пробуем добавлить в базу данных
                    return "Пользователь добавлен"  # возвращаем сообщение

                except sqlite3.IntegrityError:  # если такая запись в базе уже существуем
                    changeIntoDB(user)  # заменяем ее
                    return "Пользователь изменен"  # возвращаем сообщение

            else:  # если запись не добавлена
                return "Запись не добавлена\nНеверные данные аккаунта или профиль закрыт"

        def addToDB(user):  # добавление в базу
            db.addToBD(user)

        def changeIntoDB(user):  # изменение в базе
            db.changeIntoDB(user)

        return wrapper(message)


    @staticmethod
    def getStatistics(message):
        db = DataBase()
        userArr = db.getUser(message.author.id)
        user = User(userArr)

        def wrapper(user):
            codStat = CodStatistic()
            json = codStat.getUserStatJson(user)
            return json

        return wrapper(user)


