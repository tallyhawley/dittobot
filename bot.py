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


@bot.event
async def on_message(message):
    channel = message.channel
    if message.author == bot.user:
        return
    if message.content == "hello":
        await channel.send("<@"+ str(message.author.id) + "> world")
    if message.content == "world":
        await channel.send("<@"+ str(message.author.id) + "> hello")
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
    if message.author.bot:
        await channel.send("https://cdn.discordapp.com/attachments/602577173278228621/603650216897544201/SilenceBot.png")
    await bot.process_commands(message)


@bot.command()
async def ayaya(ctx):
    await ctx.send("ayaya!")


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


@bot.command()
async def ditto(ctx):
    await ctx.send("ditto!!!")


@bot.command()
async def bullyalex(ctx):
    await ctx.send("alex has big dumb")

bot.run(TOKEN)
