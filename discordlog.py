import discord
from discord.ext.commands import Bot
from discord.ext import commands
from time import strftime, localtime
import asyncio
import re


Client = discord.Client()
client = commands.Bot(command_prefix ="!")


@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(game=discord.Game(name='with MAIKA'))



@client.event    
async def on_message(message):    
	author = message.author
    displayname = message.author.display_name
    content = message.content
	
	if message.content.startswith('!members'):
		
		x = message.server.members
		for member in x:
			
			
			s = member.display_name
			name = member.name
			with open('names.txt', 'a', encoding='utf-8') as f:
				f.write(s + " (" + name + ") " +"\n")
					
			await client.send_message(message.channel, member.display_name)
				
				
client.run(<bot token here>)