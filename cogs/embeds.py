import discord
from discord.ext import commands

emoji_roles = {
    "❤️": 1360955286206287922,  # OV Wittgenstein
    "⚒️": 1360955338152607976,  # Stammtisch Siegen
    "✖️": 1360955506973474967  # Basisgruppe Kreuztal
}

Adminrolle = 1360736476228354150
Moderation = 1360746776306647210
Devrolle = 1360746813199614192
Vorstand = 1360749293463666861
Mitglied = 1360747087322681548

class Embeds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Sendet die Serverregeln (nur für Entwicklungs Rolle)")
    @commands.has_role(Devrolle)
    async def regeln(self, ctx):
            embed = discord.Embed(
                title="Regeln",
                color=discord.Color.red(),
                description="""Herzlich willkommen, Genoss*innen, auf dem Discord-Server des Kreisverbands DIE LINKE Siegen!\nSchön, dass ihr den Weg zu uns gefunden habt. Dieser Server dient dem Austausch, der Organisation und der Diskussion rund um unsere politische Arbeit – respektvoll, solidarisch und verbindlich.\n
                Damit sich alle hier wohlfühlen, findet ihr im Folgenden unsere Serverregeln sowie eine Übersicht zur Nutzung der einzelnen Channels.\n
                📌 Wir empfehlen außerdem einen Blick in den Channel ⁠<#1364651508305629304> zu werfen, um euch mit dem Thema Datensicherheit auseinanderzusetzen.\n
                Auf gute Gespräche, gute Organisation – und eine starke LINKE in Siegen!\n

                📜 Unsere Regeln\n
                - Bitte kommuniziert auf Deutsch oder Englisch\n- Kein Platz für Rassismus, Sexismus, Hate Speech oder Diskriminierung jeglicher Art\n- Keine Eigenwerbung (Ausnahmen nach Rücksprache möglich)\n- Keine Inhalte, die Gewalt, Pornografie, Gore, oder ähnliches zeigen\n- Die Discord-Nutzungsbedingungen (ToS) gelten auch hier\n- Bots nur nach Absprache mit dem Admin-Team\n- Keine persönlichen Daten wie Adressen oder Telefonnummern posten\n- Bitte verwendet einen sichtbaren Namen (keine unsichtbaren Nicknames)\n
                Mit freundlichen Grüßen\n<@&1360746813199614192>"""
            )
            
            # Embed mit Bildern aktualisieren
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1212498778435620924/1360750837076332664/csm_Logo_Quadrat_Die_Linke_309ebe095c.webp")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1212498778435620924/1364665255594168442/Regeln.png?ex=680a7f0f&is=68092d8f&hm=2842228ee005507e92f7dab26bffe9657539f6699313dece0e350882214a6dd1&")

            msg = await ctx.send(embed=embed)
            
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Sendet die Datenschutzrichtlinien (nur für Entwicklungs Rolle)")
    @commands.has_role(Devrolle)
    async def datenschutz(self, ctx):
            embed = discord.Embed(
                title="Datenschutz",
                color=discord.Color.purple(),
                description="""1. Welche sensiblen Daten sind wo gespeichert?\n(Sensible Daten sind beispielsweise Dokumente, Fotos, Kontaktdaten)\nPrüfe auch, ob sensible Daten auf Fotos in deiner synchronisierten Fotobibliothek vorhanden sind. (Fotos von Ausweis/Führerschein)\n
                2. Vermeide, sensible Daten auf Cloud-Speichern zu hinterlegen (Dropbox, Google Drive, iCloud)\n
                3. Achtung: Wenn du sensible Daten gelöscht hast, entferne diese auch aus dem Papierkorb\n
                4. Beschränke auch den physischen Zugriff zu Daten. (Passwörter und PINs bei Smartphones, Laptops, Desktop-Rechnern. Festplatten mit Passwörtern sichern)\n
                5. Stelle sicher und teste, dass du deine Geräte jederzeit entfernt orten und sperren kannst.\n\n

                Backups\n- Stelle sicher, dass du jederzeit den Verlust deiner Daten - beispielsweise durch Schadsoftware - auf Rechner und Smartphone verkraften kannst. (Desaster Recovery)\n- Dafür sind regelmäßige Backups von wichtigen Daten erforderlich\n- Stelle sicher, dass die Speichermedien für das Backup nicht dauerhaft mit dem Computer und/oder Netzwerk verbunden sind.\n\n

                Allgemeine Hinweise\n- Versuche, so wenig Daten wie möglich anfallen zu lassen. Daten, die nicht anfallen, können auch nicht abhanden kommen.\n- Dein persönliches Sicherheitskonzept nur so sicher wie das schwächste Glied in der Kette.\n
                Mit freundlichen Grüßen\n<@&1360746813199614192>"""
            )
            
            # Embed mit Bildern aktualisieren
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1212498778435620924/1360750837076332664/csm_Logo_Quadrat_Die_Linke_309ebe095c.webp")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1212498778435620924/1364668323723477082/Datenschutz.png?ex=680a81ea&is=6809306a&hm=fcfd6818a5dacf80ffd7acae7be9311d9b69b7955f760e759f78259d56541d97&")

            msg = await ctx.send(embed=embed)
            
            

def setup(bot):
    bot.add_cog(Embeds(bot))   