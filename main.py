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

intents = discord.Intents.all
client = discord.Client(intents=discord.Intents.all())

tree = app_commands.CommandTree(client)
# ephereal

@tree.command(name="rooli")
async def rooli(interaction: discord.Interaction):
    return

@client.event
async def on_ready():
    try:
        synced = await tree.sync()
        print("Synced tree")
    except Exception as e:
        print(e)
    print(f"Logged in as {client.user}")
    activity = discord.Game(name=f"Kehittelyssä")
    await client.change_presence(status=discord.Status.online, activity=activity)

client.run(token) # type: ignores