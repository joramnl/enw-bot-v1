@client.command()
async def create_channel(ctx):
	global isVip
	global vip_channels
	global vip_channel_users

	if not isVip:
		for x in ctx.author.roles:
			if x.id == 329352166479495180:
				isVip = True

		if not isVip:
			await ctx.channel.send(":no_entry:  <@" + str(ctx.author.id) + "> you are not a vip!")
			print(str(ctx.author) + " tried to use command: create_channel. But is not a vip")
			return None

	if ctx.author.id in vip_channel_users:
		await ctx.trigger_typing()
		await asyncio.sleep(0.05)
		await ctx.channel.send(":no_entry_sign:  You already have a channel.")
		print(str(ctx.author) + " tried to use command: create_channel. But already has a channel")
		return None

	await ctx.trigger_typing()
	await asyncio.sleep(0.05)

	print(str(ctx.author) + " used command: create_channel")

	overwrites = {
		ctx.guild.default_role: discord.PermissionOverwrite(connect=False),
		ctx.message.author: discord.PermissionOverwrite(connect=True, manage_channels=True),
		ctx.guild.me: discord.PermissionOverwrite(connect=True, manage_channels=True)
	}

	channel = await ctx.guild.create_voice_channel(str(ctx.author.name) + '\'s Channel', overwrites=overwrites, category=discord.Object(394132003173302272))
	vip_channels[ctx.author] = channel.id
	vip_channel_users.append(ctx.author.id)

	await ctx.channel.send(":loud_sound:  <@" + str(ctx.author.id) + "> your channel has been created!")

@client.command()
async def delete_channel(ctx):
	if not ctx.author.id in vip_channel_users:
		await ctx.trigger_typing()
		await asyncio.sleep(0.05)
		await ctx.channel.send(":no_entry_sign:  You don't have a channel to delete.")
		print(str(ctx.author) + " tried to use command: delete_channel. But doesnt have a channel")
		return None

	for ctx.author in vip_channels:
		channel = ctx.guild.get_channel(vip_channels[ctx.author])

	try:
		await channel.delete()
	except Exception as TheError: 
		await ctx.trigger_typing()
		await asyncio.sleep(0.05)
		await ctx.channel.send(embed=discord.Embed(title="ERROR", description=str(TheError), color=0xff0000))
	else:
		vip_channels.pop(ctx.author, None)
		vip_channel_users.remove(ctx.author.id)

		await ctx.trigger_typing()
		await asyncio.sleep(0.05)
		await ctx.channel.send(":mute:  Your channel has been deleted!")