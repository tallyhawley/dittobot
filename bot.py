import discord
import asyncio

client = discord.Client()

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
        await channel.send("world")
    if message.content.startswith("thumb"):
        channel = message.channel
        await channel.send('send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

client.run("NjAyNTc2MzE1OTE2NDg0NjE4.XTdBdg.JuB682hVxjggycCntHz70fp4dGE")