# Plans 
# Tämän hetkinen:
# Automatisoi setuppi.
# Vaihteleva RPC botille, vaihtuu joka minuutti
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

@tree.command(
        name="MC Setup",
        description="Botti rakentaa MC pohjan.",
        guild=discord.object(id=1409292359690092697),
)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync(guild=discord.Object(id=1409292359690092697))
    activity = discord.Game(name=f"Tällä hetkellä kehittämässä 'setup' komentoa.")
    await client.change_presence(status=discord.Status.online, activity=activity)

client.run(token)