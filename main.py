# Plans 
# Tämän hetkinen:
# Automatisoi setuppi.
# 1. Kun uus henkilö liityy, henkilö laittaa bottiin RP nimensä, miten pääsi servulle, ja kiinostaako jengi asiat?
# Sitten Upseeristo valitsee kyllä tai joo liittyäkseen
# 2. Vaihteleva RPC botille, vaihtuu joka minuutti
import secrets
token = secrets.token
from typing import Optional
import discord
from discord import app_commands
from discord.ext import commands
import math
import threading
import time
import asyncio

intents = discord.Intents.default() # Mitä asioita botti haluaa nähdä?
intents.message_content = True
intents.members = True
intents.guilds = True
intents.guild_messages = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync(guild=discord.Object(id=id1409292359690092697))
    activity = discord.Game(name=f"Tällä hetkellä kehittämässä 'setup' komentoa.")
    await client.change_presence(status=discord.Status.online, activity=activity)

client.run(token)