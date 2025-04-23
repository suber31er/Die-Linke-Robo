import discord
from discord.ext import commands

emoji_roles = {
    "💪": 1360753985568637148,  # Feminismus
    "🕊️": 1360754022318870799,  # Friedenspolitik
    "🚩": 1360754060353077370,  # Antifaschismus
    "⚒️": 1360754085216915728,  # Betrieb und Gewerkschaft
    "💬": 1360954903165538317,  # Sozialberatung
    "🌳": 1360954964826132642,  # Umwelt/Klima
    "🚗": 1360955008518193172,  # Verkehr
    "🤝": 1360955059315412992,  # Integration
    "✊": 1360955130907852931,  # Inklusion
    "🚜": 1360955194581712986,  # Ländlicher Raum
    "👦": 1360955242015100951,  # Jugendarbeit
    "📖": 1360955390220832808,  # Politische Bildung
    "📢": 1360955432213938309,  # Wahlkampfvorbereitung
    "🏠": 1360955564795887768,  # Wohnen muss bezahlbar bleiben
    "⛩️": 1360955621381509277,  # Kultur
    "🏳️‍🌈": 1360955669926383861,  # LGBTQIA+
    "🐨": 1360955730558976101,  # Tierschutz
    "🏫": 1360955759340421340  # Kita- und Schulbetreuungssituartion
}

Adminrolle = 1360736476228354150
Moderation = 1360746776306647210
Devrolle = 1360746813199614192
Vorstand = 1360749293463666861
Mitglied = 1360747087322681548

class Ags(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Sendet die AGS (nur für Entwicklungs Rolle)")
    @commands.has_role(Devrolle)
    async def ags_liste(self, ctx):
        try:
            embed = discord.Embed(
                title="Arbeitsgruppen",
                color=discord.Color.red(),
                description="""Sehr geehrte Genoss*innen,\nhier könnt ihr die AGs, die euch betreffen auswählen.\n
                [Feminismus💪]\n[Friedenspolitik🕊️]\n[Antifaschismus🚩]\n[Betrieb und Gewerkschaft⚒️]\n[Sozialberatung💬]\n[Umwelt/Klima🌳]\n[Verkehr🚗]\n[Integration🤝]\n[Inklusion✊]\n[Ländlicher Raum🚜]\n[Jugendarbeit👦]\n[Politische Bildung📖]\n[Wahlkampfvorbereitung📢]\n[Wohnen muss bezahlbar bleiben🏠]\nKultur⛩️]\n[LGBTQIA+🏳️‍🌈]\n[Tierschutz🐨]\n[Kita- und Schulbetreuungssituartion🏫]\n
                Mit freundlichen Grüßen\n<@&1360746813199614192>"""
            )
            
            # Embed mit Bildern aktualisieren
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1212498778435620924/1360750837076332664/csm_Logo_Quadrat_Die_Linke_309ebe095c.webp")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1212498778435620924/1360751376627404901/Arbeitsgruppen.png")

            msg = await ctx.send(embed=embed)
            
            # Bot reagiert selbst mit allen Emojis
            for emoji in emoji_roles.keys():
                await msg.add_reaction(emoji)
                
        except discord.HTTPException as e:
            print(f"HTTP Fehler: {str(e)}")
            await ctx.send("Ein HTTP-Fehler ist aufgetreten!", ephemeral=True)
        except discord.Forbidden:
            print("Keine Berechtigung zum Senden der Nachricht")
            await ctx.send("Der Bot hat keine Berechtigung zum Senden der Nachricht.", ephemeral=True)
        except Exception as e:
            print(f"Unbekannter Fehler: {str(e)}")
            await ctx.send("Ein unbekannter Fehler ist aufgetreten!", ephemeral=True)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # Prüfe direkt nach der User-ID
        if payload.user_id == self.bot.user.id:
            return
            
        # Prüfe ob die Reaktion zu unserer Nachricht gehört
        if payload.message_id:
            channel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            
            # Prüfe ob das Emoji im Mapping ist
            if str(payload.emoji) in emoji_roles:
                role_id = emoji_roles[str(payload.emoji)]
                guild = self.bot.get_guild(payload.guild_id)
                
                if guild:
                    member = guild.get_member(payload.user_id)
                    role = guild.get_role(role_id)
                    
                    if member and role:
                        await member.add_roles(role)
                        await member.send(f"Du hast erfolgreich die Rolle {role.name} erhalten!")
                        # Die Reaktion wird NICHT mehr entfernt
                        # await message.remove_reaction(payload.emoji, member)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # Prüfe direkt nach der User-ID
        if payload.user_id == self.bot.user.id:
            return
            
        # Prüfe ob die Reaktion zu unserer Nachricht gehört
        if payload.message_id:
            channel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            
            # Prüfe ob das Emoji im Mapping ist
            if str(payload.emoji) in emoji_roles:
                role_id = emoji_roles[str(payload.emoji)]
                guild = self.bot.get_guild(payload.guild_id)
                
                if guild:
                    member = guild.get_member(payload.user_id)
                    role = guild.get_role(role_id)
                    
                    if member and role:
                        await member.remove_roles(role)
                        await member.send(f"Die Rolle {role.name} wurde dir entzogen.")


def setup(bot):
    bot.add_cog(Ags(bot))   