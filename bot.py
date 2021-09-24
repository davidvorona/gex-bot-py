import discord
import json
from random import randint
from discord.ext import commands
from gex import *

#
# Get Discord bot token
#

try:
     # NOTE: add auth.json at root with the token as the only field
    # e.g. { "token": "some_random_token_value" }
    with open('auth.json', 'r') as file:
        auth_token = json.loads(file.read())['token']
except FileNotFoundError:
    print('Cannot start bot without auth token, aborting')
    raise

#
# Set basic parameters for Discord bot
#

description = "This bot reminds me of playing Scrabble at Lenny Kravitz's summer house."
# use default Discord intents
intents = discord.Intents.default()
# create bot with parameters
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

#
# Implement common bot events
#

GEX_MAX_INT = len(ALL_GEX_TEXT) - 1

@bot.event
async def on_ready():
    print('Logged in as', bot.user.name)
    print('------')

#
# Implement gex command
#

@bot.command()
async def gex(ctx):
    gex_magic_int = randint(0, GEX_MAX_INT)
    gex_text = ALL_GEX_TEXT[gex_magic_int]
    await ctx.send(gex_text)

@gex.error
async def gex_error(ctx, error):
    if (isinstance(error, commands.MissingRequiredArgument)):
        print(commands.MissingRequiredArgument)

#
# Run bot
#

bot.run(auth_token)
