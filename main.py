from discord.ext import commands
import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")

keep_alive()
bot.run(os.environ['TOKEN'])