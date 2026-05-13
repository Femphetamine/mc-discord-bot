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
    await interaction.guild.system_channel.send("'Presidentti' rooli luotu") # mitä vittua mä teen :D en ymmärrä paskaakaa

    varapresidentti = await interaction.guild.create_role(name="Varapresidentti")
    await varapresidentti.edit(colour=discord.Colour.from_str("#ab6311"), hoist=True)
    await interaction.guild.system_channel.send("'Varapresidentti' rooli luotu")

    upseeristo = await interaction.guild.create_role(name="Upseeristo")
    await upseeristo.edit(colour=discord.Colour.from_str("#000dff"), hoist=True)
    await interaction.guild.system_channel.send("'Upseeristo' rooli luotu")

    asekessu = await interaction.guild.create_role(name="Ase-kessu")
    await asekessu.edit(colour=discord.Colour.from_str("#dfdf02"), hoist=True)
    await interaction.guild.system_channel.send("'Ase-kessu' rooli luotu")

    sihteeri = await interaction.guild.create_role(name="Sihteeri")
    await sihteeri.edit(colour=discord.Colour.from_str("#00e5ff"), hoist=True)
    await interaction.guild.system_channel.send("'Sihteeri' rooli luotu")

    prospect = await interaction.guild.create_role(name="Prospect")
    await prospect.edit(colour=discord.Colour.from_str("#b8b8b8"), hoist=True)
    await interaction.guild.system_channel.send("'Prospect' rooli luotu")

    jäsen = await interaction.guild.create_role(name="Jäsen")
    await jäsen.edit(colour=discord.Colour.from_str("#9432af"), hoist=True)
    await interaction.guild.system_channel.send("'Jäsen' rooli luotu")

    sisäänpääsy = await interaction.guild.create_text_channel(name="sisäänpääsy")
    await sisäänpääsy.set_permissions(jäsen, view_channel=False, read_messages=False, send_messages=False)
    await interaction.guild.system_channel.send("'Sisäänpääsy' teksti kanava luotu")

    tiedonlähde = await interaction.guild.create_category(name="Tiedonlähde")
    await tiedonlähde.set_permissions(interaction.guild.default_role, view_channel=False, read_messages=False, send_messages=False)
    await tiedonlähde.set_permissions(jäsen, view_channel=True, read_messages=True, send_messages=False)
    await tiedonlähde.set_permissions(upseeristo, view_channel=True, read_messages=True, send_messages=True)
    await interaction.guild.system_channel.send("'Tiedönlähde' kategoria luotu")

    säännöt = await interaction.guild.create_text_channel(name="säännöt", category=tiedonlähde)
    await interaction.guild.system_channel.send("'Säännöt' teksti kanava luotu")

    hierarkia = await interaction.guild.create_text_channel(name="hierarkia", category=tiedonlähde)
    await interaction.guild.system_channel.send("'hierarkia' teksti kanava luotu")

    tiedotteet = await interaction.guild.create_text_channel(name="tiedotteet", category=tiedonlähde)
    await interaction.guild.system_channel.send("'tiedotteet' teksti kanava luotu")

    radiokanava = await interaction.guild.create_text_channel(name="radio", category=tiedonlähde)
    await interaction.guild.system_channel.send("'radio' teksti kanava luotu")

    keskustelu = await interaction.guild.create_category(name="Keskustelu")
    await keskustelu.set_permissions(interaction.guild.default_role, view_channel=False, read_messages=False, send_messages=False)
    await keskustelu.set_permissions(jäsen, view_channel=True, read_messages=True, send_messages=True)
    await interaction.guild.system_channel.send("'Keskustelu' kategoria luotu")

    ooc = await interaction.guild.create_text_channel(name="ooc", category=keskustelu)
    await interaction.guild.system_channel.send("'ooc' teksti kanava luotu")
    
    media = await interaction.guild.create_text_channel(name="media", category=keskustelu)
    await interaction.guild.system_channel.send("'media' teksti kanava luotu")

    puh = await interaction.guild.create_voice_channel(name="Puhelu", category=keskustelu)
    await interaction.guild.system_channel.send("'Puhelu' teksti kanava luotu")

    upseeristoKategoria = await interaction.guild.create_category(name="Upseeristo")
    await upseeristoKategoria.set_permissions(interaction.guild.default_role, view_channel=False, read_messages=False, send_messages=False)
    await upseeristoKategoria.set_permissions(jäsen, view_channel=True, read_messages=False, send_messages=False)
    await upseeristoKategoria.set_permissions(upseeristo, view_channel=True, read_messages=True, send_messages=True)

    upooc = await interaction.guild.create_text_channel(name="upooc", category=upseeristoKategoria)
    await interaction.guild.system_channel.send("'upseeristo_ooc' teksti kanava luotu")

    dev = await interaction.guild.create_text_channel(name="dev", category=upseeristoKategoria)
    await interaction.guild.system_channel.send("'dev' teksti kanava luotu")

    channel = discord.utils.get(interaction.guild.channels, name="säännöt")
    channel_id = channel.id
    await channel.send("--  Kunnioita hierarkiaa  --\n" \
        "1. Presidentin sana on laki.\n"
        "2. Varapresidentti johtaa presidentin poissa ollessa.\n"
        "3. Toimi roolisi sisällä, ellei muuten sanottu. (Jos ketään ei ole specifissä roolissa, voit toimia omasi ja vapaan roolin sisällä\n" \
        "\n"
        "-- Käyttäytyminen --\n"
        "1. Kunnioita kaikkia jäseniä, jokainen jäsen on yhtä tärkeä. NAISIA EI LOUKATA/HAKATA.\n"
        "2. Ei selän takana puhumista, luottamuss on kaiken perusta.\n" \
        "3. Edusta MC:tä vaatetuksella.\n" \
        "\n" \
        "-- Seuraukset --\n" \
        "Sääntöjen jatkuva rikkominen seuraa erotus.")
    await interaction.guild.system_channel.send("Säännöt lisätty")

    channel = discord.utils.get(interaction.guild.channels, name="hierarkia")
    channel_id = channel.id
    await channel.send("Presidentti -- Johtaa ja edustaa klubia, päätökset tehdään yhdessä upseeriston kanssa.\n" \
        "\n" \
        "Varapresidentti -- Ottaa presidentin vallan tilapäisesti haltuun kun presidentti ei ole paikalla\n" \
        "\n" \
        "Upseeristo -- Ei kuvausta\n" \
        "\n" \
        "Ase-kessu -- Ei kuvausta\n" \
        "\n" \
        "Sihteeri -- Ei kuvausta\n" \
        "\n" \
        "Prospect -- Ei kuvausta\n" \
        "\n" \
        "Jäsen -- Ei kuvausta")
    
    channel = discord.utils.get(interaction.guild.channels, name="sisäänpääsy")
    channel_id = channel.id
    await channel.send("Kirjoita - !!Roolini - tälle kanavalle, botti tarkistaa oletko jo listattu jäseneksi ja mihin rooliin pääset, saat automaattisesti roolin.")

    await interaction.guild.system_channel.send("Hierarki teksti lisätty")
    await interaction.guild.system_channel.send("-- Pohja valmis!")

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