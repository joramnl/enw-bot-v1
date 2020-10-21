import discord
from discord.ext import commands
import asyncio
from decimal import Decimal

class Utility:

	def __init__(self, bot):
		self.client = bot



	@commands.command(brief='Replies back with a pong')
	@commands.guild_only()
	async def ping(self, ctx):
		"""Command which replies back with a pong"""

		try:
			await ctx.trigger_typing()
			await asyncio.sleep(0.05)

			print(str(ctx.author) + " used command: ping")

			await ctx.send(':ping_pong: Pong! ({}ms)'.format(round(self.client.latency * 1000)))
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000))



	@commands.command(brief='Shows your UserID')
	@commands.guild_only()
	async def userid(self, ctx):
		"""Command which shows someones userid"""

		try:
			await ctx.trigger_typing()
			await asyncio.sleep(0.05)

			print(str(ctx.author) + " used command: userid")

			await ctx.send(":1234:  <@" + str(ctx.author.id) + "> your UserID is: " + str(ctx.author.id) + "!")
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000))



	@commands.command(brief='Tells you how to get a VIP role')
	@commands.guild_only()
	async def vip(self, ctx):
		"""Command which shows how to get the vip role"""

		try:
			await ctx.trigger_typing()
			await asyncio.sleep(0.05)

			print(str(ctx.author) + " used command: vip")

			#Create embed
			vip_message_embed = discord.Embed(title="Linking Discord", description="To get a VIP role on discord you need to connect your Discord ID with the VIP system.  Doing this is fairly easy.", color=0x0080ff)
			vip_message_embed.set_author(name="Extreme-Network", icon_url=ctx.guild.me.avatar_url)
			vip_message_embed.add_field(name='Step 1', value='Type `enw.userid` and hit enter.', inline=True)
			vip_message_embed.add_field(name='Step 2', value='Copy ID and navigate to your VIP profile (https://www.extreme-network.net/vip/?viewmyprofile=1)', inline=True)
			vip_message_embed.add_field(name='Step 3', value='Look for the Discord section, paste your ID in the input box and hit \'Send\'', inline=True)
			vip_message_embed.set_footer(text="If you've done these steps correctly, and you have an active VIP subscription. The bot will update your roles within a minute.")

			#Send message
			await ctx.send(embed=vip_message_embed, delete_after=60)
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000), delete_after=60)



def setup(client):
	client.add_cog(Utility(client))