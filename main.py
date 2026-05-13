# Plans 
# Tämän hetkinen:
# Automatisoi setuppi.
# Vaihteleva RPC botille, vaihtuu joka minuutti
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

from typing import Optional
import discord
import discord.ext
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all
client = discord.Client(intents=discord.Intents.all())

tree = app_commands.CommandTree(client)

@tree.command(name="test")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olen hereillä! {interaction.user.mention}")

@tree.command(name="setupserver")
async def setupserver(interaction: discord.Interaction):
    print(f"Setupserver")
    await interaction.response.send_message("Odotappa hetki...")
    await interaction.guild.create_role(name="Presidentti")
    await interaction.guild.system_channel.send("Presidentti luotu")

@client.event
async def on_ready():
    try:
        synced = await tree.sync()
        print("Synced tree")
    except Exception as e:
        print(e)
    print(f"Logged in as {client.user}")
    activity = discord.Game(name=f"Tällä hetkellä kehittämässä 'setup' komentoa.")
    await client.change_presence(status=discord.Status.online, activity=activity)

client.run(token) # type: ignore