import traceback
import sys
from discord.ext import commands
import discord


class CommandErrorHandler:
	def __init__(self, bot):
		self.client = bot



	async def on_command_error(self, ctx, error, member: discord.Member=None):
		"""The event triggered when an error is raised while invoking a command.
		ctx   : Context
		error : Exception"""


		if hasattr(ctx.command, 'on_error'):
			return

		error = getattr(error, 'original', error)

		
		if isinstance(error, commands.CommandNotFound):

			if not member:
				member = ctx.author

			#Create the embed
			not_found_embed = discord.Embed(title='\uFEFF', color=0xff0000)
			not_found_embed.set_author(icon_url=member.avatar_url, name=str(member))
			not_found_embed.add_field(name='Error', value=str(error), inline=True)
			not_found_embed.set_thumbnail(url="https://i.imgur.com/aSVjtu7.png")

			#Delete original message
			await ctx.message.delete()

			#Send message
			return await ctx.send(embed=not_found_embed, delete_after=60)

		elif isinstance(error, commands.UserInputError):

			if not member:
				member = ctx.author

			#Create the embed
			user_input_embed = discord.Embed(title='\uFEFF', color=0xff8000)
			user_input_embed.set_author(icon_url=member.avatar_url, name=str(member))
			user_input_embed.add_field(name='Error', value='Missing arguements', inline=True)

			#Delete original message
			await ctx.message.delete()

			#Send message
			return await ctx.send(embed=user_input_embed, delete_after=60)

		elif isinstance(error, commands.DisabledCommand):

			if not member:
				member = ctx.author

			#Create the embed
			disabled_command_embed = discord.Embed(title='\uFEFF', color=0xff5706)
			disabled_command_embed.set_author(icon_url=member.avatar_url, name=str(member))
			disabled_command_embed.add_field(name='Error', value='Sorry! "{}" has been disabled.'.format(ctx.command), inline=True)

			#Delete original message
			await ctx.message.delete()

			#Send message
			return await ctx.send(embed=disabled_command_embed, delete_after=60)

		elif isinstance(error, commands.NoPrivateMessage):
			try:
				return await ctx.author.send('{} can not be used in Private Messages.'.format(ctx.command))
			except:
				pass
			
		print('Ignoring exception in command {}:'.format(ctx.command))
		traceback.print_exception(type(error), error, error.__traceback__)
		


def setup(client):
	client.add_cog(CommandErrorHandler(client))