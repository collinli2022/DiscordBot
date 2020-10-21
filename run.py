import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
import random
import json 
import helper # self-written helper module

cc = helper.getJson('dablitfam.json') # commands that can be easily changed from json
headers = helper.getHeaderAliases(cc)

command_prefix = '>'
client = commands.Bot(command_prefix = command_prefix)
## EVENTS
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_member_join(ctx, member):
    await ctx.send(f'{member} is now part of our cult')

## DEBUG FUNCTIONS

## ALL COMMANDS
@client.event # While an event, it actually does custom commands
async def on_message(message):
    if message.content[0] == command_prefix:
        print(message.content)
        daContent = ''
        if ' ' in message.content:
            daMessage = message.content[1:message.content.index(' ')] # grab the command
            daContent = message.content[message.content.index(' '):] # grab the other stuff after command
        else:
            daMessage = message.content[1:]

        # custom commands start here
        if daMessage in headers:
            await message.channel.send(helper.getResponse(daMessage, cc))
        elif daMessage in ['8ball', 'ask']:
            await message.channel.send(helper._8ball(daContent))
        elif daMessage in ['love']:
            if '<@!' in daContent and '>' in daContent:
                user = daContent[daContent.index('!')+1:daContent.index('>')]
                #user = await client.fetch_user(int(user))
                user = await helper.getUser(client, user)
                await message.channel.send(message.author.mention + ':heart:' + user.mention)
            else:
                #user = await client.fetch_user(767928423183417364)
                user = await helper.getUser(client, 767928423183417364)
                await message.channel.send(message.author.mention + ':heart:' + user.mention)
        else: # custom commands end here
        	await client.process_commands(message)
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
@commands.command(aliases=['commandlist', 'commands'])
async def _help(self, ctx):
    await ctx.send_help()
@client.command()
async def changeStatus(ctx, arg1, arg2):
	await helper.changeStatus(client, arg1, arg2)
	await ctx.send('Changed Status')

token = helper.getToken()
client.run(token) # Add token here
print("end")
