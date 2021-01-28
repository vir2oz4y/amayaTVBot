from DataBase import DataBase
from Statistic.CodTracker import CodTracker
from User import User
import discord

class Statistic:
    db = DataBase()
    codTracker = CodTracker()
    channel_name = 'статистика-warzone'
    commands = ['!up', '!reg', ]

    def start(self, message):
        if message.channel.name != self.channel_name:
            return
        elements = self.getElementsMessage(message)
        userDB = self.db.check_user(User(message.author.id,None,None))


        if userDB is not None:
            user = User(userDB[0], userDB[1], userDB[2])
            if elements[0] == self.commands[0]:
                stats = self.get_stats(user)
                return self.MessageStats(stats, user.wz_name, message)
            elif elements[0] == self.commands[1]:
                mes = 'Вы уже зарегистрированы'
                return mes
            else:
                mes = 'Неверная комманда'
                return mes
        else:
            if len(elements) != 2 and not elements[0] != self.commands[1]:
                mes = 'Неверные данные'
                return mes
            else:
                user = User(message.author.id,elements[1][0], elements[1][1])
                if self.codTracker.check_acc(user):
                    self.db.insert_into_DB(user)
                    return 'Вы зарегистрированы!'
                else:
                    mes = 'Данный аккаунт не существует'
                    return mes

    def MessageStats(self, *args):
        warzone = args[0].warzone_info
        embed = discord.Embed(
            title='Warzone',
            colour=discord.Colour.blue()
        )
        embed.set_thumbnail(url=args[2].author.avatar_url)
        embed.set_author(name=args[1])
        embed.add_field(name='🔪Убийств', value=warzone.kills, inline=True)
        embed.add_field(name='💀Смертей', value=warzone.deaths, inline=True)
        embed.add_field(name='Нокдаунов', value=warzone.downs, inline=False)
        embed.add_field(name='KDA', value=warzone.kda, inline=False)
        embed.add_field(name='Винрейт', value=warzone.wr, inline=False)
        embed.add_field(name='🥇Побед', value=warzone.wins, inline=True)
        embed.add_field(name='🥈top5', value=warzone.top5, inline=True)
        embed.add_field(name='🥉top10', value=warzone.top10, inline=True)
        embed.add_field(name='⏱️Среднее время жизни', value=warzone.avgLife, inline=False)

        return embed

    def getElementsMessage(self, message):
        content = message.content
        elements = content.split(' ')

        try:
            elements[1] = elements[1].split('#')
        except IndexError:
            pass
        return elements


    # register new account
    def register(self, user):
        if self.codTracker.check_acc(user):  # check what account is exists in tracker
            if self.db.check_user(user):  # check what account in db if in UPDATE else INSERT
                self.db.update_DB(user)
            else:
                self.db.insert_into_DB(user)
            return True
        else:
            return False

    def get_stats(self, user):
        return self.codTracker.get_stats(user)  # get stats from codTracker


if __name__ == '__main__':
    pass
