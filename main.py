# Plans 
# 1. Kun uus henkilö liityy, henkilö laittaa bottiin RP nimensä, miten pääsi servulle, ja kiinostaako jengi asiat?
# Sitten Upseeristo valitsee kyllä tai joo liittyäkseen
# 2. Vaihteleva RPC botille, vaihtuu joka minuutti

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

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")  
    activity = discord.Game(name=f"Kerho elää!", 
    large_image="https://i.imgur.com/E8hOFp1.jpeg",
    large_text = "Kerho Elää!",
    details = "024",
    state="Mä oon vieläki tässä pelissä, nii älä äiti itke")
    await client.change_presence(status=discord.Status.online, activity=activity)

# @client.command()
# async def PohjaSetup(ctx): # Luo MC Kerhon Pohja, roolit ja kanavat.
#     print(f"Pohjasetup aloitettu klo {time.strftime}")
#     pass

client.run("MTUwMzc3NzIxNTYyMjQxODQ5NA.GEaT7J.bsdF_pfIRMbF-oa9cVSNBGE1x_HC9Lvd_exbvo")