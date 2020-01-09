import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("I'm a Honkai")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('k.hello'):
        await message.channel.send('내가 왔노라.')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
