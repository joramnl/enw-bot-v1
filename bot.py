# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
from datetime import date
from datetime import datetime,timedelta
import discord
import asyncio
from contextlib import suppress
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import sys, traceback

initial_extensions = ['cogs.owner', 'cogs.fun', 'cogs.utility', 'cogs.error_handler']

client = Bot(description="ENW BOT", command_prefix="enw.", pm_help = True)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print("Failed to load extension {}.".format(extension))
            traceback.print_exc()

@client.event
async def on_ready():
	print('Logged in as {} (ID: {})'.format(client.user.name, client.user.id))

	bot_presence = client.command_prefix + "help | exteme-network.net"
	print("Changing presence to: " + bot_presence)
	await client.change_presence(game=discord.Game(name=bot_presence))


#Secet bot token
client.run('token', bot=True, reconnect=True)