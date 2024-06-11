#Imported libaries to run a discord bot
import discord
from discord.ext import commands, tasks
#Open files to be able to read contents
on_ready_file = open("Data/on_ready.txt", "r")
commandprefix_file = open("Data/commandprefix.txt", "r")
commands_file = open("Data/commands.txt", "r")
responses_file = open("Data/responses.txt", "r")
#Gets the options you set from the Data folder
token = open("Data/token.txt", "r").read()
channelid = int(open("Data/channelid.txt", "r").read())
prefix = commandprefix_file.read()
command = commands_file.readlines()
responses = responses_file.readlines()
#Set the bot intent
bot = commands.Bot(command_prefix=prefix,intents=discord.Intents.all())
#When bot is ready this event is triggered
@bot.event
async def on_ready():
    #Tells when the bot has logged in through the terminal
    print(f'We have logged in as {bot.user}')
    #Gets the channel that the id was set to
    channel = bot.get_channel(channelid)
    #If there is a on ready message it will be sent
    if on_ready_file.read().strip() != "":
        await channel.send(open("Data/on_ready.txt", "r").read())
    #Starts the loop
    await auto_send.start(channel)
#Loops infinitely
@tasks.loop(seconds=0)
async def auto_send(channel : discord.TextChannel):
    #If a channel message is sent through the discord manager the bot will send the message and then remove it so it doesn't send forever
    message_file = open("Data/message.txt", "r")
    if message_file.read().strip() != "":
        await channel.send(open("Data/message.txt", "r").read())
        message_file = open("Data/message.txt", "w")
        message_file.write("")
    message_file.close()
#When a message is sent this event is triggered
@bot.event
async def on_message(message):
    #If message is from bot ingore
    if message.author == bot.user:
        return     
    #Gets the channel that the id was set to
    channel = bot.get_channel(channelid)
    line = 0    
    #If a message starts with the prefix it'll go through a list of commands and if it matches it'll send a corresponding message else it'll send Unknown Command
    if message.content.startswith(prefix):
        for i in command:
            if message.content.startswith(prefix + i.strip()):
                await channel.send(responses[line])
                return
            line+=1
        await channel.send("Unknown Command")
#Initialize the bot
bot.run(token)