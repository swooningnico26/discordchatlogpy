import discord
from discord.ext.commands import Bot
from discord.ext import commands
from time import strftime, localtime
import asyncio

from itertools import cycle
import re


Client = discord.Client()
client = commands.Bot(command_prefix ="!")



async def change_status():
    await client.wait_until_ready()
    quotesHonk = cycle(quotes)
    statusVar = cycle(status)

    while not client.is_closed:
        current_quote = next(quotesHonk)
        current_status = next(statusVar)

        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)
        
        
@client.event
async def on_ready():
    print('Bot is ready')
    

async def format_message(message):
   
    msg = "**<{0.author}>** {0.content}".format(message)
    
    timestamp = strftime("%Y-%m-%d", localtime())
    log = "<{0.author}> {0.content}".format(message, timestamp)
    if message.attachments:
        
        img = message.attachments[0]['url']
        msg += " {}".format(img)
        log += " {}".format(img)

    return msg, log

async def relay_message(msg, channel_id):
    await client.send_message(client.get_channel(channel_id), msg)

def write(log, _file):
    print(log, file=open(_file, "a", encoding="utf-8"))


async def log_discord(message, relay_id, _file):
    msg, log = await format_message(message)
    await relay_message(msg, relay_id)
    write(log, _file)

@client.event   
async def on_message_delete(message):

    channel = message.channel.id
    auid = message.author.id
    author = message.author
    displayname = message.author.display_name
    content = message.content
    timestamp = strftime("%Y-%m-%d", localtime())
    timestampwithtime = strftime("%a, %d %b %Y %H:%M:%S +08", localtime())

    embed = discord.Embed(title="{} <{}> ({})".format(displayname, author, auid), description="<@{}>".format(auid), color=0x00ff00)
    embed.add_field(name="Message:", value="{}".format(content), inline=False)
    embed.add_field(name="Channel:", value="<#{}>".format(channel), inline=False)
    embed.add_field(name="Date and Time:", value="{}".format(timestampwithtime), inline=False)
    embed.set_thumbnail(url="<IMAGE_URL_HERE>")
    #embed.set_image(url="{}".format(img))
    await client.send_message(discord.Object(id='<LOGS_CHANNEL_ID_HERE>'), embed=embed)

    
    print('{} ({}): {}'.format(displayname,author,content))
    
    
@client.event    
async def on_message(message):
    
    
    channel = message.channel.id
    auid = message.author.id
    author = message.author
    displayname = message.author.display_name
    content = message.content
    timestamp = strftime("%Y-%m-%d", localtime())
    timestampwithtime = strftime("%a, %d %b %Y %H:%M:%S +08", localtime())

    if not message.author.id == "<THIS_BOT_ID>": #bot id #so that it wont log the chat from this bot 
        if not message.channel.id == "<CHANNEL_ID_NOT_TO_LOG_HERE>": #lewd-lobby #a channel that you don't want to log
            #await log_discord(message, "473064460764971017", "{}.txt".format(timestamp))
            await log_discord(message, "<WASTE_CHANNEL_ID_HERE>", "logs/{}.txt".format(timestamp))


            embed = discord.Embed(title="{} <{}> ({})".format(displayname, author, auid), description="<@{}>".format(auid), color=0x00ff00)
            embed.add_field(name="Message:", value="{}".format(content), inline=False)
            embed.add_field(name="Channel:", value="<#{}>".format(channel), inline=False)
            embed.add_field(name="Date and Time:", value="{}".format(timestampwithtime), inline=False)
            embed.set_thumbnail(url=IMAGE_URL_HERE)
            #embed.set_image(url="{}".format(img))
            await client.send_message(discord.Object(id="<LOGS_CHANNEL_ID_HERE>"), embed=embed)


   

    
     
client.loop.create_task(change_status())

client.run("<BOT_TOKEN_HERE>")
