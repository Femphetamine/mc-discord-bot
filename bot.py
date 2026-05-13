# Plans 
# 1. Kun uus henkilö liityy, pistää bottiin RP nimensä, miten pääsi servulle, ja kiinostaako jengi asiat?

from typing import Optional

import discord.ext
import time
from discord import app_commands
true = True
false = False
spam = false

intents = discord.Intents.default() # Mitä asioita botti haluaa nähdä?
intents.message_content = True
intents.members = True
intents.guilds = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event  
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("test"):
        print("Terminal test ping")
        spam = true
        while spam == true:
            await message.channel.send("valkosuomi voimaan!")
        time.sleep(2)
        spam = false
        return

client.run("MTUwMzc3NzIxNTYyMjQxODQ5NA.GEaT7J.bsdF_pfIRMbF-oa9cVSNBGE1x_HC9Lvd_exbvo")