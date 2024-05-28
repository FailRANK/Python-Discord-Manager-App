import discord
from discord.ext import commands, tasks

import asyncio

#Open files to be able to read contents
on_ready_file = open("Data/on_ready.txt", "r")
commandprefix_file = open("Data/commandprefix.txt", "r")
commands_file = open("Data/commands.txt", "r")
responses_file = open("Data/responses.txt", "r")

command = commands_file.readlines()
responses = responses_file.readlines()

#Change token to your bot
token = open("Data/token.txt", "r").read()
channelid = open("Data/channelid.txt", "r").read()
prefix = commandprefix_file.read()
bot = commands.Bot(command_prefix=prefix,intents=discord.Intents.all())

#when bot is ready this event is triggered
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(channelid)
    List = on_ready_file.readlines()
    if List:
        await channel.send(List[0])
    await auto_send.start(channel)

@tasks.loop(seconds=1)
async def auto_send(channel : discord.TextChannel):
    message_file = open("Data/message.txt", "r")
    List = message_file.readlines()
    if List:
        await channel.send(List[0])
        message_file = open("Data/message.txt", "w")
        message_file.write("")
    message_file.close()
#when a message is sent this event is triggered
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return     
    channel = bot.get_channel(channelid)
    line = 0    
    if message.content.startswith(prefix):
        for i in command:
            if message.content.startswith(prefix + i.strip()):
                await channel.send(responses[line])
                return
            line+=1
        await channel.send("Unkown command")
#initialize the bot
bot.run(token)