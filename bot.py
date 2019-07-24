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
    if message.author.bot or message.author.id == 404119987939180554:
        await channel.send("https://cdn.discordapp.com/attachments/602577173278228621/603650216897544201/SilenceBot.png")
    await bot.process_commands(message)


@bot.command()
async def ayaya(ctx):
    await ctx.send("ayaya! <:ayaya:603654847799099393>")


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


@bot.command()
async def ditto(ctx):
    await ctx.send("ditto!!!")


@bot.command()
async def bullyalex(ctx):
    await ctx.send("alex has big dumb")


@bot.command()
async def OwO(ctx):
    await ctx.send("What's this?")

@bot.command()
async def AYAYA(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/571351447795400707/603699021755842687/New_video.mp4")

@bot.command()
async def copypasta(ctx):
    await ctx.send("What the fuck did you just fucking say about me, you little bitch? I'll have you know "
                   "I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on "
                   "Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top "
                   "sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe "
                   "you the fuck out with precision the likes of which has never been seen before on this Earth, mark "
                   "my fucking words. You think you can get away with saying that shit to me over the Internet? Think "
                   "again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP "
                   "is being traced right now so you better prepare for the storm, maggot. The storm that wipes out "
                   "the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime,"
                   " and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I "
                   "extensively trained in unarmed combat, but I have access to the entire arsenal of the United "
                   "States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face "
                   "of the continent, you little shit. If only you could have known what unholy retribution your "
                   "little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking "
                   "tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will "
                   "shit fury all over you and you will drown in it. You're fucking dead, kiddo.")

bot.run(TOKEN)
