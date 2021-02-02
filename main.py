import discord
from discord.ext import commands
from setting import botToken
from User import  User
from discordCommands import DiscordCommands

class MyClient(discord.Client):
    clients = commands.Bot(command_prefix='!')
    myCommands = ['!reg', '!up']

    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('Call Of Duty: Warzone'))
        print('Logger')


    async def on_message(self, message):
        if message.author == client.user:  # если сообщение отправляет бот то оно игнорируется
            return

        def reg_command(discordMessage):  # команда регистрации
            return DiscordCommands.registration(discordMessage)  # возврашает сообщение о добавлении или изменении данных в БД

        def get_statistics(discordMessage):
            return DiscordCommands.getStatistics(discordMessage)

        if message.channel.name == 'статистика-warzone':  # если канал статистики
            command = message.content.split(' ')[0]  # получили введенную команду

            if command not in self.myCommands:  # если этой команды нет в списке
                await message.delete()  # удаляем сообщение

            else:
                if command == '!reg':  # если !reg
                    chatMessage = reg_command(message)  # сообщение для откправки равно сообшению выполнения команды
                    await message.channel.send(chatMessage)  # Отправляем сообшение в канал

                if command == '!up':
                    chatMessage = get_statistics(message)
                    await message.channel.send(chatMessage)  # Отправляем сообшение в канал




client = MyClient()
client.run(botToken)
