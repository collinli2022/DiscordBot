import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
import random
import json

# DISCORD HELP

# PERSONAL HELP
def getJson(location):
	# Opening JSON file 
	with open(location, 'r') as openfile: 
		# Reading from json file 
		commands = json.load(openfile)
	return commands
	
def getToken():
	fname = 'token.txt' # txt location
	with open(fname, 'r') as f:
		for line in f:
			print('token is:', line)
			return line
			
def getHeaderAliases(jsonObject):
	headers = []
	for i in jsonObject:
		headers.append(i)
	return headers

def getResponse(name, jsonObject):
	return random.choice(jsonObject[name])

def _8ball(question):
	responses = ['It is certain',
               'It is decidedly so',
               'Without a doubt',
               'Yes – definitely',
               'You may rely on it',
               'As I see it, yes',
               'Most likely',
               'Outlook good',
               'Yes Signs point to yes',
               'Reply hazy',
               'try again',
               'Ask again later',
               'Better not tell you now',
               'Cannot predict now',
               'Concentrate and ask again',
               'Dont count on it',
               'My reply is no',
               'My sources say no',
               'Outlook not so good',
               'Very doubtful',
               'Simp harder']
	return 'Question: ' + question + '\nAnswer: ' + random.choice(responses)