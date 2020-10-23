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


client.run(config('SECRET_TOKEN'))
