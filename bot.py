import discord
from discord.ext import commands
import asyncio
import os
import random
import wit

BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ['token']

bot = commands.Bot(command_prefix=BOT_PREFIX)
wit = wit.Wit("V7ITRHN3CSZZJ6WNOHCOMX2V4NC2ZJG6") # add wit.ai implementation


@bot.event
async def on_ready():
    print("The bot is ready!")
    await bot.change_presence(activity=discord.Game(name="wit yo feelings"))

@bot.command()
async def ayaya(ctx):
    await ctx.send("ayaya! <:ayaya:603654847799099393>")


@bot.command()
async def echo(ctx, *, content: str):
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
        await channel.send(
            "https://cdn.discordapp.com/attachments/602577173278228621/603650216897544201/SilenceBot.png")
    await bot.process_commands(message)

@bot.command()
async def copypasta(ctx):
    # select a random copypasta
    a = random.randint(1, 4)
    if a == 1:
        await ctx.send("What the fuck did you just fucking say about me, you little bitch? I'll have you know "
                       "I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids "
                       "on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the "
                       "top sniper in the entire US armed forces. You are nothing to me but just another target. I "
                       "will wipe you the fuck out with precision the likes of which has never been seen before on "
                       "this Earth, mark my fucking words. You think you can get away with saying that shit to me over "
                       "the Internet? Think again, fucker. As we speak I am contacting my secret network of spies "
                       "across the USA and your IP is being traced right now so you better prepare for the storm, "
                       "maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking "
                       "dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and "
                       "that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I "
                       "have access to the entire arsenal of the United States Marine Corps and I will use it to its "
                       "full extent to wipe your miserable ass off the face of the continent, you little shit. If only "
                       "you could have known what unholy retribution your little \"clever\" comment was about to bring "
                       "down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, "
                       "and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will "
                       "drown in it. You're fucking dead, kiddo.")
    elif a == 2:
        await ctx.send("The Watts–Strogatz model is a random graph generation model that produces graphs with "
                       "small-world properties, including short average path lengths and high clustering. It was "
                       "proposed by Duncan J. Watts and Steven Strogatz in their joint 1998 Nature paper.[1] The model "
                       "also became known as the (Watts) beta model after Watts used beta to formulate it in his "
                       "popular science book Six Degrees.")
    elif a == 3:
        await ctx.send("Runaway now is not OWL level, as fanboy-triggering as that sounds. People loved them for their "
                       "underdog streak, and their vibrant brand/personality, but expecting them to get pick up is "
                       "very unrealistic. They still have to actually win something first. At the same time, I'd "
                       "honestly advise Flowervin to sell Bumper, Stitch and Haksal and then rebuild. Those buyouts "
                       "money can help Runaway for a few more season.")
    elif a == 4:
        await ctx.send("I’ve fled my hometown, changed my number and stolen a 2018 Ford Fiesta, but nothing seems to "
                       "be working. I uninstalled the Duolingo app 5 days ago, but I still get the notifications "
                       "demanding me to learn Spanish. On the third day, I heard a window downstairs break and found a "
                       "brick on the floor. There was a note tied to it saying,”Your time is almost up. Learn the "
                       "fucking mexican words or else”. I don’t have the work ethic to dedicate the effort to learn "
                       "the language, and just accepted my fate. But the next day, when I found the brakes in my car "
                       "removed after causing a minor accident at a nearby intersection, I realized that I’m afraid to "
                       "die. In that very moment, I received another notification saying,“It’s too late for practice "
                       "now. Speak the Spanish all you want, I will make sure of tu muerte”. I then turned around to "
                       "see what I swear was a mass of neon green feathers dart behind a tree. I did not sleep that "
                       "night, and I’m thankful for it. A few hours after I went to bed, the owl appeared in my "
                       "window, but quickly fled after I drew my firearm from my nightstand. That’s when I decided it "
                       "was time to leave, and later stole a car parked down my street. But I know that my fate is "
                       "sealed. Because every second I’m not running, he’s only getting closer. The notifications from "
                       "the deleted duolingo app have been getting progressively darker and more sinister. The last one"
                       " didn’t even ask me to practice learning my language. It was just the owl asserting to me that "
                       "he is God. I know I’ll die soon. I’ve accepted it. Yet I’m still upset that my life has to end "
                       "because of my inability to learn Spanish.")


bot.run(TOKEN)
