import discord
from discord.ext import commands
from decouple import config

client = commands.Bot(command_prefix='/')
client.remove_command('help')


@client.event
async def on_ready():
    print('Bot is now online.')


@client.command()
async def help(ctx, *, to='server'):
    embed = discord.Embed(
        title='Ambassador | Help',
        description="run commands by using '/' at prefix",
        color=discord.Color.orange()
    )
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/avatars/766224438513369109/6477b9c304caa29f2124f993c0f0817b.png?size=256')
    embed.add_field(name='help', value='get help about bot in server')
    embed.add_field(name='help `direct`', value='get help about bot in direct')
    embed.add_field(name='ping', value='get bot latency')
    embed.add_field(name='clear `int`', value='clear messages on server')
    embed.add_field(name='kick `member` `reason`', value='kick member out of server', inline=True)
    embed.add_field(name='ban `member` `reason`', value='ban member from server', inline=True)
    embed.add_field(name='unban `user#id`', value='unban member for server', inline=True)
    embed.set_footer(text='https://github.com/harshcut')
    if to == 'direct':
        author = ctx.message.author
        await discord.User.send(author, embed=embed)
    elif to == 'server':
        await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f'Bot Latency : {round(client.latency * 1000)}ms')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    if amount < 1:
        await ctx.send("How do you do that?")
    elif amount == 1:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Deleted {amount} message!')
    else:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Deleted {amount} messages!')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Argument is not a number!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing permissions to manage messages.")
    else:
        print(error)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} from Server!\nReason : {reason}')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Member not found!")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("You can't run this task!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing permissions to kick members.")
    else:
        print(error)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} from Server!\nReason : {reason}')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Member not found!")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("You can't run this task!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing permissions to ban members.")
    else:
        print(error)


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned! {user.mention} can now join server through an invite link.')
            return
    await ctx.send(f"Can't find `{member}` in banned members!")


@client.command()
async def get(ctx, server, attribute):
    if server == 'server':
        if attribute == 'name':
            await ctx.send(f'Server Name : `{ctx.guild.name}`')
        elif attribute == 'id':
            await ctx.send(f'Server ID : `{ctx.guild.id}`')
        elif attribute == 'region':
            await ctx.send(f'Server Region : `{ctx.guild.region}`')
        elif attribute == 'count':
            await ctx.send(f'Server Member Count : `{ctx.guild.member_count}`')


client.run(config('SECRET_TOKEN'))
