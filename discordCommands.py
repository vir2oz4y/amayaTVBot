from Statistics import CodStatistic
from dataBase.DataBase import DataBase
from User import User
from StatisticInfo.userInfo import Stats
import datetime
import discord
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
        user.avatar_url = message.author.avatar_url

        def wrapper(user, message):
            codStat = CodStatistic()
            json = codStat.getUserStatJson(user)
            try:
                userStats = getUserStats(json)
                return getEmbed(userStats, user, message)
            except:
                return "Аккаунт введен неверно"

        def getUserStats(jsonObject):
            return Stats(jsonObject)

        def getEmbed(userStats, user, message):
            embed = discord.Embed(title="Статистика Warzone",
                                  colour=discord.Colour.blue()
                                  )
            emojiDeath = message.guild.emojis[0]
            emojiKills = message.guild.emojis[1]
            emojiKD = message.guild.emojis[2]
            emojiCountMatches = message.guild.emojis[3]
            emojiAvgLife = message.guild.emojis[4]
            emojiCountContr = message.guild.emojis[5]
            emojiWR = message.guild.emojis[6]


            embed.set_author(name=user.fullname)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text=str(datetime.datetime.now()))
            embed.add_field(name=f"{emojiCountMatches}Матчей сыграно:", value=userStats.warzone_info.gamesPlayed, inline=False)
            embed.add_field(name=f"{emojiAvgLife}Среднее время жизни в игре:", value=userStats.warzone_info.avgLife, inline=False)
            embed.add_field(name=f"{emojiCountContr}Выполнено контрактов:", value=userStats.warzone_info.contracts, inline=False)
            embed.add_field(name=f"{emojiKills}Убийств:", value=userStats.warzone_info.kills, inline=False)
            embed.add_field(name=f"{emojiDeath}Смертей:", value=userStats.warzone_info.deaths, inline=False)
            embed.add_field(name=f"{emojiKD}K/D", value=userStats.warzone_info.kda, inline=False)
            embed.add_field(name=":first_place:Побед:", value=userStats.warzone_info.wins, inline=False)
            embed.add_field(name=f"{emojiWR}Процент побед:", value=userStats.warzone_info.wr, inline=False)
            embed.add_field(name=":slot_machine:Очков в минуту:", value=userStats.warzone_info.scorePerMinute, inline=False)
            return embed

        return wrapper(user, message)


