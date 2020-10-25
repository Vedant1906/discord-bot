import discord
from discord.ext import commands
from decouple import config

client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    print('Bot is now online.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Bot Latency : {round(client.latency * 1000)}ms')


@client.command()
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


client.run(config('SECRET_TOKEN'))
