# Plans 
# 1. Kun uus henkilö liityy, pistää bottiin RP nimensä, miten pääsi servulle, ja kiinostaako jengi asiat?

from typing import Optional

import discord
from discord import app_commands

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
    # New Command
    if message.content.startswith("!!##SetupSäännöt"):
        await message.channel.send("--  Kunnioita hierarkiaa  --\n" \
        "1. Presidentin sana on laki.\n"
        "2. Varapresidentti johtaa presidentin poissa ollessa.\n"
        "3. Toimi roolisi sisällä, ellei muuten sanottu.\n" \
        "\n"
        "-- Käyttäytyminen --\n"
        "1. Kunnioita kaikkia jäseniä, jokainen jäsen on yhtä tärkeä. NAISIA EI LOUKATA/HAKATA.\n"
        "2. Ei selän takana puhumista, luottamuss on kaiken perusta.\n" \
        "3. Kilpailevien jengien tai MC:iden kanssa ei toimita ilman lupaa.\n" \
        "4. Rikollisuutta ei tehdä liivit tai tunnistettavilla vaatteilla. vaihda ajoneuvot, vaatteet ja naamioidu ennen rikollisuutta. Autot hävitetään rikoksien jälkeen.\n" \
        "\n" \
        "-- Seuraukset --\n" \
        "Sääntöjen jatkuva rikkominen seuraa erotus, ja päädyt tappo listalle.")
    # New Command
    if message.content.startswith("!!##SetupKysyJäsenyys"):
        await message.channel.send("Kirjoita tähän RP nimesi, ja kenen kautta pääsit serverille.")
    # New Command
    if message.content.startswith("!!##SetupHierarkia"):
        await message.channel.send("<@&1503768215514386575> -- Johtaa ja edustaa klubia, päätökset tehdään yhdessä upseeriston kanssa.\n" \
        "\n" \
        "<@&1503768703593087037> -- Presidentin tuki, osallistuu päätöksiin ja hoitaa asiat kun presidentti ei paikalla.\n" \
        "\n" \
        "<@&1503806572214751232> -- Ei kuvausta\n" \
        "\n" \
        "<@&1503769082028232845> -- Ei kuvausta\n" \
        "\n" \
        "<@&1503768975174144020> -- Ei kuvausta\n" \
        "\n" \
        "<@&1503769417706766386> -- Ei kuvausta")


client.run("MTUwMzc3NzIxNTYyMjQxODQ5NA.GEaT7J.bsdF_pfIRMbF-oa9cVSNBGE1x_HC9Lvd_exbvo")