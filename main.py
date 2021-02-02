import discord
from discord.ext import commands
from setting import botToken
from User import  User


class MyClient(discord.Client):
    clients = commands.Bot(command_prefix='!')

    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('call of duty: Warzone'))
        print('Logger')

    async def on_message(self, message):
        if message.author == client.user:
            return
        user = User.userFromMessage(message)
        print(message.content)



client = MyClient()
client.run(botToken)
