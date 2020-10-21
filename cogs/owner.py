import discord
from discord.ext import commands


class OwnerCog:

	def __init__(self, bot):
		self.client = bot
	
	# Hidden means it won't show up on the default help.
	@commands.command(name='load', hidden=True)
	@commands.is_owner()
	async def cog_load(self, ctx, *, cog: str):
		"""Command which Loads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			#Delete original message
			await ctx.message.delete()

			self.client.load_extension(cog)
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000), delete_after=5)
		else:
			await ctx.send(embed=discord.Embed(title="Done!", description="Loaded: {}".format(cog), color=0x00ff00), delete_after=5)

	@commands.command(name='unload', hidden=True)
	@commands.is_owner()
	async def cog_unload(self, ctx, *, cog: str):
		"""Command which Unloads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			#Delete original message
			await ctx.message.delete()
			
			self.client.unload_extension(cog)
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000), delete_after=5)
		else:
			await ctx.send(embed=discord.Embed(title="Done!", description="Unloaded: {}".format(cog), color=0x00ff00), delete_after=5)

	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def cog_reload(self, ctx, *, cog: str):
		"""Command which Reloads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			#Delete original message
			await ctx.message.delete()

			self.client.unload_extension(cog)
			self.client.load_extension(cog)
		except Exception as e:
			await ctx.send(embed=discord.Embed(title=str(type(e).__name__), description=str(e), color=0xff0000), delete_after=5)
		else:
			await ctx.send(embed=discord.Embed(title="Done!", description="Reloaded: {}".format(cog), color=0x00ff00), delete_after=5)


def setup(client):
	client.add_cog(OwnerCog(client))