# Plans 
# Tämän hetkinen:
# Automatisoi setuppi.
# Vaihteleva RPC botille, vaihtuu joka minuutti
import secrets
token = secrets.token
from typing import Optional
import discord
import discord.ext
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.bot(command_prefix="!", intents = discord.intents.all())

@bot.tree.command(name="test")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Päivää sullekki")

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands!")
    except Exception as e:
        print(e)

    activity = discord.Game(name=f"Tällä hetkellä kehittämässä 'setup' komentoa.")
    await client.change_presence(status=discord.Status.online, activity=activity)

client.run(token)