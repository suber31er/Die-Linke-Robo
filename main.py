import discord
from discord.ext import commands
import time
import os
import dotenv

dotenv.load_dotenv()

# Verwaltungsrollen
Adminrolle = 1360736476228354150
Moderation = 1360746776306647210
Devrolle = 1360746813199614192
Vorstand = 1360749293463666861
Mitglied = 1360747087322681548

# Channel IDs
Rollen = ""  
Regeln = ""
Verifizierung = ""

# Timer für Bot-Laufzeit
start_time = None

# Intents konfigurieren
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

# Bot initialisieren
client = discord.Bot(intents=intents)


cogs_list = [
    'ags',
    'zusatz',
    'embeds'
]

for cog in cogs_list:
    client.load_extension(f'cogs.{cog}')

def start_timer():
    """Startet den Timer."""
    global start_time
    start_time = time.time()

def get_runtime():
    """Gibt die Laufzeit des Bots in Sekunden zurück."""
    global start_time
    if start_time is None:
        return 0
    current_time = time.time()
    runtime = current_time - start_time
    return round(runtime, 2)

start_timer()

@client.event
async def on_ready():
    print(f'Erfolgreich eingeloggt als {client.user}')
    print(f'Bereitschaftsstatus: {client.status}')
    print('Verfügbare Guilds:')
    for guild in client.guilds:
        print(f'- {guild.name} (ID: {guild.id})')

@client.command(description="Testet die Bot-Funktionalität")
async def test(ctx):
    try:
        rounded_latency = round(client.latency * 1000)  # Latenz in ms
        embed = discord.Embed(
            title="Bot Status",
            color=discord.Color.green(),
            description=f"""**Der bot ist Online**
Ping: **{rounded_latency}ms**
Online: **{get_runtime()}** Sekunden"""
        )
        await ctx.send(embed=embed)
    except Exception as e:
        print(f"Fehler beim Test-Kommando: {str(e)}")
        await ctx.send("Ein Fehler ist aufgetreten!", ephemeral=True)



# Bot starten
client.run(str(os.getenv("TOKEN")))
