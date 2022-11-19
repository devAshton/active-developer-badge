import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()


bot = commands.Bot()

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' (' + str(bot.user.id) + ')')

@bot.slash_command(description="Replies with pong!")
async def badge(interaction: nextcord.Interaction):
    await interaction.send("**This is a test command to get the Active Developer Badge!**\nYou will be able to claim your Active Developer Badge within 24 hours\n\n**Make sure to subscribe to cdnAshton for making this method!**\nhttps://youtube.com/c/cdnashton\n\nhttps://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge", ephemeral=True)

bot.run(os.getenv("TOKEN"))