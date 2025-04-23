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

class Zusatz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Sendet die Zusatzrollen (nur für Entwicklungs Rolle)")
    @commands.has_role(Devrolle)
    async def zusatz(self, ctx):
        try:
            embed = discord.Embed(
                title="Zusatzrollen",
                color=discord.Color.red(),
                description="""Sehr geehrte Genoss*innen,\nhier könnt ihr die Zusatzrollen, die euch betreffen auswählen.\n
                [OV Wittgenstein❤️]\n[Stammtisch Siegen⚒️]\n[Basisgruppe Kreuztal✖️]\n
                Mit freundlichen Grüßen\n<@&1360746813199614192>"""
            )
            
            # Embed mit Bildern aktualisieren
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1212498778435620924/1360750837076332664/csm_Logo_Quadrat_Die_Linke_309ebe095c.webp")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1212498778435620924/1364648019278041218/Zusatzrollen.png?ex=680a6f01&is=68091d81&hm=cae6c98db6612fbe3e7413cf0042ba01beab05ab56afc48eca22baf0eb69dfff&")

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
    bot.add_cog(Zusatz(bot))   