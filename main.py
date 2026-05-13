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
from discord import Permissions, app_commands

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

    presidentti = await interaction.guild.create_role(name="Presidentti")
    await presidentti.edit(colour=discord.Colour.from_str("#a8150a"), hoist=True)
    await interaction.guild.system_channel.send("Presidentti rooli luotu") # mitä vittua mä teen :D en ymmärrä paskaakaa

    varapresidentti = await interaction.guild.create_role(name="Varapresidentti")
    await varapresidentti.edit(colour=discord.Colour.from_str("#ab6311"))
    await interaction.guild.system_channel.send("Varapresidentti rooli luotu")

    asekessu = await interaction.guild.create_role(name="Ase-kessu")
    await asekessu.edit(colour=discord.Colour.from_str("#dfdf02"))
    await interaction.guild.system_channel.send("Ase-kessu rooli luotu")

    Sihteeri = await interaction.guild.create_role(name="Sihteeri")
    await Sihteeri.edit(colour=discord.Colour.from_str("#00e5ff"))
    await interaction.guild.system_channel.send("Sihteeri rooli luotu")

    Prospect = await interaction.guild.create_role(name="Prospect")
    await Prospect.edit(colour=discord.Colour.from_str("#b8b8b8"))
    await interaction.guild.system_channel.send("Prospect rooli luotu")

    Prospect = await interaction.guild.create_role(name="Jäsen")
    await Prospect.edit(colour=discord.Colour.from_str("#9432af"))
    await interaction.guild.system_channel.send("Jäsen rooli luotu")

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