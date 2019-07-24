import discord
from discord.ext import commands
import asyncio
import os

BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ['token']

client = commands.Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="test"))


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return
    if message.content == "hello":
        await channel.send("<@"+ str(message.author.id) + "> world")
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


@client.command()
async def ayaya(ctx):
    await ctx.send("ayaya!")

client.run(TOKEN)
