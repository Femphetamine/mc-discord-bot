import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    activity = discord.Game(name=f"Paikalla")
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run(token) # type: ignores