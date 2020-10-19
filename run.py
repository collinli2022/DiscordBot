import discord
from discord.ext import commands

client = discord.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
client.run('your token here') # Add token here