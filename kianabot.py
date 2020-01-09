import discord

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

client.run('NjY0Njg0MTEzOTY1MzUwOTIz.XhbGOQ.0mP45a1RXwL9lTsUUV1S5PLFr4M')