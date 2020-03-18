import discord
from discord.ext import commands
import asyncio
import os
import random
from markov_chain_generator import MarkovGenerator
import csv
from urllib.request import urlopen
import codecs

BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ['token']

bot = commands.Bot(command_prefix=BOT_PREFIX)

generators = {}

swears = ["fuck", "shit", "bitch", "pussy", "dick", "cunt", "whore", "cock", "piss"]
prefixes = ['!', '.', ';', '?', '$', '%', '^', '&', '*', '/', ',', '~', '-', '+', '>', '<', 'p!']
banned_words = ['gusting', 't.co', 'humidity', '#', '@', '&amp;', '&lt;', 'ud', 'temperature', 'barometer',
                'graffiti tracking', 'nigga', '°f', 'wind', 'north york']

url = 'https://dittobot.s3-us-west-1.amazonaws.com/dashboard_x_usa_x_filter_nativeretweets.csv'
tweets = urlopen(url)
tweetreader = list(csv.reader(codecs.iterdecode(tweets, 'utf-8')))


async def init_generator(guild: discord.Guild):
    generator = MarkovGenerator(2, 50)
    generators[guild] = generator
    messages = []
    for channel in guild.channels:
        if channel.type == discord.ChannelType.text:
            try:
                async for message in channel.history(limit=500000):
                    if not message.author.bot:
                        has_prefix = False
                        for prefix in prefixes:
                            if message.content.startswith(prefix):
                                has_prefix = True
                                break
                        if not has_prefix:
                            messages.append(message.content.lower())
            except:
                pass
    for message in messages:
        found = False
        for word in banned_words:
            if word in message:
                found = True
                break
        if not found:
            generators[guild].feed(message)
            generators[guild].feed(message)
            generators[guild].feed(message)
    for row in tweetreader[1:]:
        try:
            if row[17] == 'en':
                found = False
                for word in banned_words:
                    if word in row[6]:
                        found = True
                        break
                if not found and not row[6].startswith("wind"):
                    generators[guild].feed(row[6].lower())
        except IndexError:
            continue

@bot.event
async def on_ready():
    print("the bot is ready!")
    await bot.change_presence(activity=discord.Game(name="wit yo feelings"))

@bot.command()
async def ayaya(ctx):
    await ctx.send("ayaya! <:ayaya:603654847799099393>")


@bot.command()
async def echo(ctx, *, content: str):
    await ctx.send(content)


@bot.command()
async def ditto(ctx):
    await ctx.send(generators[ctx.message.guild].generate())


@bot.command()
async def bullyalex(ctx):
    await ctx.send("alex has big dumb")


@bot.command()
async def owo(ctx):
    await ctx.send("what's this?")

@bot.command()
async def initialize(ctx):
    guild = ctx.guild
    await init_generator(guild)
    await ctx.send("initialized!")


@bot.command()
async def id(ctx, *members: commands.Greedy[discord.Member]):
    if len(members) == 0:
        await ctx.send("<@" + str(ctx.author.id) + "> " + str(ctx.author.id))
    else:
        await ctx.send("<@" + str(ctx.author.id) + "> " + ', '.join(str(member.id) for member in members))

@bot.event
async def on_message(message):
    channel = message.channel
    if message.author == bot.user:
        return
    if message.content == "hello":
        await channel.send("<@" + str(message.author.id) + "> world")
    if message.content == "world":
        await channel.send("<@" + str(message.author.id) + "> hello")
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
    # if message.author.bot or message.author.id == 404119987939180554:
    # await channel.send("https://cdn.discordapp.com/attachments/602577173278228621/603650216897544201/SilenceBot.png")
    if message.author.bot:
        await channel.send("begone, bot")
    for swear in swears:
        if message.content.lower().find(swear) >= 0:
            await channel.send("watch yo motherfuckin language")

    await bot.process_commands(message)

bot.run(TOKEN)
