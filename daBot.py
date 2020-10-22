import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
import random
import json 
import helper # self-written helper module


# python3 /home/pi/Desktop/DiscordBot/run.py
cc = helper.getJson('/home/pi/Desktop/DiscordBot/dablitfam.json') # commands that can be easily changed from json
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
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("**SHUTTING DOWN... Astalavista Babyy!!**")
    await ctx.bot.logout()

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
        elif daMessage in ['testDelete']:
            await message.delete()
        elif daMessage in ['say'] and message.author.id == 401494858985897995:
            await message.delete()
            await message.channel.send(message.content[message.content.index(' '):])


        else: # custom commands end here
            await client.process_commands(message)
    else: # normal message (no command_prefix)
         # anti bully
        if 'collin' in message.content.lower():
            reply, sentiment = helper.bullyCollin(message.content)
            print()
            print("ANTI BULLY - message: \""+message.content)
            print(sentiment)
            if(len(reply) > 0):
                await message.channel.send(reply)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
@commands.command(aliases=['commandlist', 'commands'])
async def _help(self, ctx):
    await ctx.send_help()
@client.command(aliases=['status'])
async def changeStatus(ctx, arg1, arg2):
    await helper.changeStatus(client, arg1, arg2)

token = helper.getToken()
client.run(token) # Add token here
print("end")
