import discord
import time
import random

client = discord.Client()
sec = [3,2,1,0]


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('k.help|| Honkai impact 3rd'))
    print('We have logged in as {0.user}'.format(client))


async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'k.hello' or message.content == 'K.hello':
        await message.channel.send('人類よ、用がないのなら私の邪魔をするな\n인류여, 용무가 없다면 나를 방해하지 말거라.')

    if message.content == 'k.help' or message.content == 'K.help':
        embed = discord.Embed(title="Kiana bot Commands", description="키아나 봇 명령어 설명입니다", color=0x00ff00)
        embed.add_field(name="k.help", value="봇 명령어를 보여줍니다", inline=False)
        embed.add_field(name="k.hello", value="봇에게 인사합니다", inline=False)
        embed.set_footer(text="Last update 2020/01/16")
        embed.set_thumbnail(url=client.user.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == 'k.clear' or message.content == 'K.clear':
        if client.has_permissions(manage_messages=True):
            amount = 11
            await message.channel.purge(limit=amount)
            await message.channel.send(f'10개의 메세지는 내가 없앴다.')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
