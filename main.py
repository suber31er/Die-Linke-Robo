import discord
import discord.ext
import discord.ext.commands
from discord.ext import tasks
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
import random
import time
import json
import os
import asyncio

# Verwaltungsrollen
Adminrolle = ""
Moderation = ""
Vorstand = ""
Mitglied = ""

#Channel
Rollen = ""
Regeln = ""
Verifizierung = ""

#Zusatzrollen

#---------------------------------------------------------------------------------------------------------------------------------------------
start_time = None
intents = discord.Intents.default()
intents.message_content = True

client = discord.Bot(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
def get_runtime():
    """Gibt die Laufzeit des Bots in Sekunden zurück."""
    global start_time
    if start_time is None:
        pass
    else:
        current_time = time.time()
        runtime = current_time - start_time
        return round(runtime, 2)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Commands

@client.command(description="Sendet eine Testnachricht")
async def test(interaction):
    rounded_latency = round(client.latency)
    embed = discord.Embed(title="Bot Status", color=discord.Color.green(),
    description=f"**Der bot ist Online** \nPing: **{rounded_latency}** \nOnline: **{get_runtime()}** Sekunden")
    await interaction.response.send_message(embed=embed,ephemeral=False)



client.run('BOT TOKEN')