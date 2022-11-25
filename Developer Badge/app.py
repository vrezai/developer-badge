import discord
from discord.ext import commands

bot = discord.Bot()

# Creating an event in the console for when the bot is online!


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

# A discord slash command. /ping: says "Pong!"


@bot.slash_command
async def ping(ctx):
    await ctx.respond("Pong!")

bot.run('')
