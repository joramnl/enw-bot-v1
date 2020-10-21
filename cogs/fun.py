import discord
from discord.ext import commands
import asyncio
import random


class Fun:

	def __init__(self, bot):
		self.client = bot



	@commands.command(brief='Shows memes about Schwarz.')
	@commands.guild_only()
	async def schwarz(self, ctx):
		"""Command which shows memes of Schwarz"""

		try:
			await ctx.trigger_typing()
			await asyncio.sleep(0.05)

			print(str(ctx.author) + " used command: schwarz")

			schwarzpictures = [
				discord.File('./images/schwarz1.png'),
				discord.File('./images/schwarz2.png'),
				discord.File('./images/schwarz3.png')
			]

			await ctx.channel.send(file=random.choice(schwarzpictures))
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000))



	@commands.command(brief='Shows memes about Shibe.')
	@commands.guild_only()
	async def shibe(self, ctx):
		"""Command which shows memes of Riri"""

		try:
			await ctx.trigger_typing()
			await asyncio.sleep(0.05)

			print(str(ctx.author) + " used command: shibe")

			shibepictures = [
				discord.File('./images/shibe1.png'),
				discord.File('./images/shibe2.png'),
				discord.File('./images/shibe3.png'),
				discord.File('./images/shibe4.png'),
				discord.File('./images/shibe5.png'),
				discord.File('./images/shibe6.png'),
				discord.File('./images/shibe7.jpg'),
				discord.File('./images/shibe8.jpg'),
				discord.File('./images/shibe9.jpg'),
				discord.File('./images/shibe (8).jpg'),
				discord.File('./images/shibe (9).jpg'),
				discord.File('./images/shibe (10).jpg'),
				discord.File('./images/shibe (11).jpg'),
				discord.File('./images/shibe (12).jpg'),
				discord.File('./images/shibe (13).jpg'),
				discord.File('./images/shibe (14).jpg'),
				discord.File('./images/shibe (15).jpg'),
				discord.File('./images/shibe (16).jpg'),
				discord.File('./images/shibe (17).jpg'),
				discord.File('./images/shibe (18).jpg'),
				discord.File('./images/shibe (19).jpg'),
				discord.File('./images/shibe (20).jpg'),
				discord.File('./images/shibe (21).jpg'),
				discord.File('./images/shibe (22).jpg'),
				discord.File('./images/shibe (23).jpg'),
				discord.File('./images/shibe (24).jpg'),
				discord.File('./images/shibe (25).jpg'),
				discord.File('./images/shibe (26).jpg'),
				discord.File('./images/shibe (27).jpg'),
				discord.File('./images/shibe (28).jpg'),
				discord.File('./images/shibe (29).jpg'),
				discord.File('./images/shibe (30).jpg'),
				discord.File('./images/shibe (31).jpg'),
				discord.File('./images/shibe (32).jpg'),
				discord.File('./images/shibe (33).jpg')
			]

			await ctx.send(file=random.choice(shibepictures))
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000))



	@commands.command(brief='Shows memes about how bad anime really is.')
	@commands.guild_only()
	async def weebs(self, ctx):
		"""Command which shows about how bad anime really is"""

		try:
			await ctx.trigger_typing()
			await asyncio.sleep(0.05)

			print(str(ctx.author) + " used command: weebs")

			weebpictures = [
				discord.File('./images/weebs1.png'),
				discord.File('./images/weebs2.png'),
				discord.File('./images/weebs3.png'),
				discord.File('./images/weebs4.png'),
				discord.File('./images/weebs5.png')
			]

			weebquotes = [
				':no_entry_sign: BAN ALL WEEBS!',
				':crossed_swords: I shall destroy anime',
				':question: Why do people get obessed with anime...'
			]

			await ctx.send(random.choice(weebquotes), file=random.choice(weebpictures))
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000))



	@commands.command(brief='Throws a sick dab in the chat.')
	@commands.guild_only()
	async def dab(self, ctx):
		"""Command which throws a sick dab"""

		try:
			await ctx.trigger_typing()
			await asyncio.sleep(0.05)

			print(str(ctx.author) + " used command: dab")

			await ctx.send(file=discord.File('./images/dab.png'))
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000))



def setup(client):
	client.add_cog(Fun(client))