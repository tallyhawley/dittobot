import discord
from discord.ext import commands
import asyncio
import os

BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ['token']

bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_ready():
    print("The bot is ready!")
    await bot.change_presence(activity=discord.Game(name="wit yo feelings"))
    await bot.change_presence(activity=discord.Game(name="test"))


@bot.event
async def on_message(message):
    channel = message.channel
    if message.author == bot.user:
        return
    if message.content == "hello":
        await channel.send("<@"+ str(message.author.id) + "> world")
    if message.content.startswith("thumb"):
        await channel.send('send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

bot.run(TOKEN)
