import discord
from discord.ext import commands
from setting import botToken



class MyClient(discord.Client):
    clients = commands.Bot(command_prefix='!')

    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('call of duty: Warzone'))
        print('Logger')

    async def on_message(self, message):
        if message.author == client.user:
            return
        print(message.author.id)



client = MyClient()
client.run(botToken)
