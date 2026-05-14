# UUDELLEEN KOODAUS VITTU TÄÄ ON PERSEESTÄ
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

from typing import Optional
import discord
import discord.ext
from discord.ext import commands
from discord import Permissions, app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# ephereal

@bot.command()
async def päivitä_säännöt(ctx, *, arg, number):
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

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    activity = discord.Game(name=f"Kehittelyssä")
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run(token) # type: ignores