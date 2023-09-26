import discord
import time
import datetime

with open("token.txt", "r") as f: # reads the token from the token.txt file. 
    token = f.read()

day = datetime.datetime.today().weekday()


intents = discord.Intents.default() # sets the intents of the bot. intents are a form of permissions for the bot
intents.message_content = True # allows the bot to read messages.
intents.members = True # allows the bot to read members.
intents.presences = True # allows the bot to read the presence of members.
intents.guilds = True # allows the bot to read the guilds.
intents.reactions = True # allows the bot to read reactions.


client = discord.Client(intents=intents)

@client.event 
async def on_ready(): # event that runs when the bot is ready to use. 
    print(f'We have logged in as {client.user}') 

async def on_message(message): # event that runs when a message is sent. 
    if message.author == client.user: # if the message is sent by the bot, return. 
        return

    if message.content.startswith('hello'): # checks for a user message
        await message.channel.send('Hi :3') # sends a message to the channel

async def day(message):
    if day == 4:
        await message.channel.send('It\'s Flatworm Friday!')
        #await message.channel.send('FLATWORM.MP4 LINK')
    
client.run(token) #starts the bot with the token in the token.txt file.