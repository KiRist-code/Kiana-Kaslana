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
    if message.content.startswith('K.hello'):
        await message.channel.send('내가 왔노라.')

@client.event
async def on_message(message):
    if message.content.startswith('k.help'):
        embed = discord.Embed(color=808000)
        embed.add_field(name="Commands", value="These are kianabot command", inline =False)
        embed.add_field(name="k.help", value="명령어를 확인합니다.", inline =False)
        embed.add_field(name="k.hello", value="봇에게 인사를 합니다.", inline=False)
        embed.add_field(name="이 이후의 명령어는 추후에 개발됩니다.",value="last update 2020/1/9", inline=False)
        embed.set_thumbnail(url=client.user.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith('K.help'):
        embed = discord.Embed(color=808000)
        embed.add_field(name="Commands", value="These are kianabot command", inline =False)
        embed.add_field(name="k.help", value="명령어를 확인합니다.(K.help 도 가능)", inline =False)
        embed.add_field(name="k.hello", value="봇에게 인사를 합니다.(K.hello 도 가능)", inline=False)
        embed.add_field(name="이 이후의 명령어는 추후에 개발됩니다.",value="last update 2020/1/9", inline=False)
        embed.set_thumbnail(url=client.user.avatar_url)
        await message.channel.send(embed=embed)

client.run('NjY0Njg0MTEzOTY1MzUwOTIz.XhbhRA.ubyVh0pgSZop0NdrC_saNC0Wjow')
