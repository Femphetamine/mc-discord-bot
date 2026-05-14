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
    if ctx.author.id == 980559850234843177 or 684389100790349939:
        channel = discord.utils.get(ctx.guild.channels, name="säännöt")
        print(f"!päivitä_säännöt käytettiin")
        await channel.send(arg)
    else:
        await ctx.send("Haista vittu!")
        return
    
@bot.command()
async def lähetä_tiedotteet(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177 or 684389100790349939:
        channel = discord.utils.get(ctx.guild.channels, name="tiedotteet")
        print(f"!lähetä_tiedotteet käytettiin")
        await channel.send(arg)
    else:
        await ctx.send("Haista vittu!")
        return
    
@bot.command()
async def lähetä_hierarkia(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177 or 684389100790349939:
        channel = discord.utils.get(ctx.guild.channels, name="hierarkia")
        print(f"!lähetä_hierarkia käytettiin")
        await channel.send(arg)
    else:
        await ctx.send("Haista vittu!")
        return
    
@bot.command()
async def lähetä_radio(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177 or 684389100790349939:
        channel = discord.utils.get(ctx.guild.channels, name="radio")
        print(f"!lähetä_radio käytettiin")
        await channel.send(arg)
    else:
        await ctx.send("Haista vittu!")
        return

@bot.command()
async def lähetä_rooli(ctx, *, arg):
    if ctx.author == bot.user:
        return
    if ctx.author.id == 980559850234843177 or 684389100790349939:
        channel = discord.utils.get(ctx.guild.channels, name="roolit")
        print(f"!päivitä_roolit käytettiin")
        await channel.send(arg)
    else:
        await ctx.send("Haista vittu!")
        return

@bot.command() # Muista lisätä uusia tehtyjä komentoja!
async def apua(ctx):
    if ctx.author == bot.user:
        return
    await ctx.send("prefix = $  |   $lähetä_radio, $lähetä_hierarkia, $lähetä_tiedotteet, $lähetä_rooli $apua")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    activity = discord.Game(name=f"Paikalla")
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run(token) # type: ignores