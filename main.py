import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

from typing import Optional
import discord
import discord.ext
from discord.ext import commands
from discord import Permissions, app_commands # en tiiä tarviiko näitä, en haluu koskea.

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.command()
async def lähetä_säännöt(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177:
        channel = discord.utils.get(ctx.guild.channels, name="säännöt")
        print(f"!päivitä_säännöt käytettiin")
        await channel.send(arg)
    else:
        print("Error")
        await ctx.send("Haista vittu!")
        return
    
@bot.command()
async def lähetä_tiedotteet(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177:
        channel = discord.utils.get(ctx.guild.channels, name="tiedotteet")
        print(f"!päivitä_säännöt käytettiin")
        await channel.send(arg)
    else:
        print("Error")
        await ctx.send("Haista vittu!")
        return
    
@bot.command()
async def lähetä_hierarkia(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177:
        channel = discord.utils.get(ctx.guild.channels, name="hierarkia")
        print(f"!päivitä_säännöt käytettiin")
        await channel.send(arg)
    else:
        print("Error")
        await ctx.send("Haista vittu!")
        return
    
@bot.command()
async def lähetä_radio(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177:
        channel = discord.utils.get(ctx.guild.channels, name="radio")
        print(f"!päivitä_säännöt käytettiin")
        await channel.send(arg)
    else:
        print("Error")
        await ctx.send("Haista vittu!")
        return

@bot.command()
async def apua(ctx):
    if ctx.author == bot.user:
        return
    await ctx.send("prefix = $  |   $lähetä_radio, $lähetä_hierarkia, $lähetä_tiedotteet, $apua")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    activity = discord.Game(name=f"Kehittelyssä")
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run(token) # type: ignores