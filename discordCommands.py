from Statistics import CodStatistic
from dataBase.DataBase import DataBase
from InfoLastMatch.InfoLastMatch import InfoLastMatch, CommandStats
from functools import reduce
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
    def createUser(message):  # функция создания пользователя
        db = DataBase()
        userArr = db.getUser(message.author.id)
        user = User(userArr)
        user.avatar_url = message.author.avatar_url
        return user

    @staticmethod
    def getStatisticsLastMatch(message):
        user = DiscordCommands.createUser(message)  # user
        codStat = CodStatistic()  # class for codStatistic
        infoUserAboutLastMatch = codStat.getLastMatchJson(user)
        matchId = infoUserAboutLastMatch['id']  # получили id матча
        infoAboutAllUsers = codStat.getMatchByIDJson(matchId)['match']['segments']


        def getTop3command(allCommands):  # возвращает массив из первых 3 мест матча
            commands = list(filter(lambda x: x['placement']['value'] <= 3, allCommands))  # получаем игроков призовых мест

            command1 = list(filter(lambda x: x['placement']['value'] == 1, commands))
            command2 = list(filter(lambda x: x['placement']['value'] == 2, commands))
            command3 = list(filter(lambda x: x['placement']['value'] == 3, commands))
            command1stats = CommandStats(command1)
            command2stats = CommandStats(command2)
            command3stats = CommandStats(command3)
            return [command1stats, command2stats, command3stats]

        def getUrlLobby(kd):  # получить url рейтинга лобби по его кд
            urls = ['https://i.ebayimg.com/00/s/MTAyNFgxMjgw/z/s~4AAOxySoJTRPQK/$_1.JPG?set_id=8800005007',
                    'https://kartinkinaden.ru/uploads/posts/2020-07/1593793012_8-p-fon-serebro-13.jpg',
                    'https://storage.needpix.com/rsynced_images/yellow-corner-fading-background.jpg',
                    'https://img.pngio.com/diamond-backgrounds-wallpaper-cave-diamond-background-images-png-3840_2160.png']  # бронза, серебро, золото, алмаз

            kds = [[0.00, 0.80],[0.81,0.90],[0.91,1.15], [1.21, 555]]  # значения кд для каждого рейтинга
            index = 0
            for i in kds:
                if  kd >= i[0] and kd <= i[1]:
                    return urls[index]
                index+=1


        def getEmbed(user ,userInfo, allGamersLastMatch):
            avgKD = round(reduce(lambda x, y: x + y['statistics']['kdRatio'], infoAboutAllUsers, 0) / len(infoAboutAllUsers), 2)  # получили среднее кд лобби
            top3Commands = getTop3command(allGamersLastMatch)  # объукты команд первых 3 мест
            infoLastMatch = InfoLastMatch(userInfo)  # информация о прошлом матче

            emojiDeath = message.guild.emojis[0]
            emojiKills = message.guild.emojis[1]
            emojiKD = message.guild.emojis[2]
            emojiWR = message.guild.emojis[6]

            embed = discord.Embed(title="Статистика Последней игры Warzone",
                                  colour=discord.Colour.blue()
                                  )
            embed.set_author(name=infoLastMatch.nickName)
            embed.set_thumbnail(url=getUrlLobby(avgKD))
            embed.set_footer(text=str(datetime.datetime.now()))


            embed.add_field(name=f"{emojiKills}Убийств:", value=infoLastMatch.kills, inline=True)
            embed.add_field(name=f"{emojiKills}Помощи:", value=infoLastMatch.assists, inline=True)
            embed.add_field(name=f"{emojiKills}Урона нанесено:", value=infoLastMatch.damageDone, inline=True)

            embed.add_field(name=f"{emojiDeath}Смертей:", value=infoLastMatch.deaths, inline=False)
            embed.add_field(name=f"{emojiKD}K/D:", value=infoLastMatch.kd, inline=False)
            embed.add_field(name=f"{emojiKD}Среднее K/D матча:", value=str(avgKD), inline=False)

            embed.add_field(name=f"{emojiWR}Место в матче:", value=infoLastMatch.placement, inline=False)
            embed.add_field(name="Победа в гулаге:", value='Да' if infoLastMatch.gulagWin else 'Нет', inline=False)

            embed.add_field(name="Информация о победителях:", value=f":first_place:\nУбийств {emojiKills} : {top3Commands[0].kills}\nСреднее К\Д {emojiKD} :  {top3Commands[0].avgKDPerMatch} \n"
                                                                    f":second_place:\nУбийств {emojiKills} : {top3Commands[1].kills}\nСреднее К\Д {emojiKD} :  {top3Commands[1].avgKDPerMatch} \n"
                                                                    f":third_place:\nУбийств {emojiKills} : {top3Commands[2].kills}\nСреднее К\Д:  {top3Commands[2].avgKDPerMatch} \n")

            return  embed

        return getEmbed(user, infoUserAboutLastMatch, infoAboutAllUsers)




    @staticmethod
    def getStatisticsUser(message):
        user = DiscordCommands.createUser(message)  # user

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


