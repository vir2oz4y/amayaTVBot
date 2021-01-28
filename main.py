import discord
from discord.ext import commands

from setting import botToken
from DataBase import DataBase
from Statistic.Statistic import Statistic




class MyClient(discord.Client):
    db = DataBase()
    statistic = Statistic()
    clients = commands.Bot(command_prefix='!')

    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('Выносит мусор из канала!'))
        print('Logger')

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('!reg') or message.content.startswith('!up'):
            mess = self.statistic.start(message)
            await message.channel.send(embed=mess)
        else:
            await message.delete()
            return



client = MyClient()
client.run(botToken)
