import discord
import asyncio
import os

BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ['token']

client = discord.Client(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="wit yo feelings"))


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return
    if message.content == "hello":
        await channel.send("<"+ message.author.id + "> world")
    if message.content.startswith("thumb"):
        await channel.send('send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

client.run(TOKEN)
