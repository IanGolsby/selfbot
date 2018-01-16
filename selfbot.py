import discord
from discord.ext import commands

token = "I got hacked so I'm changing this the fuck up and now new token and not putting that on github again cause I was tired last night when I pushed the update"
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("-----")

    #await client.change_presence(game=discord.Game(name="Discord.py"))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        # General Commands
        if message.content.startswith('>help'):
            await client.send_message(message.channel, '**Commands List:**\n`>help` - sends this message. Lists all commands.\n`>purge [x]` - deletes x messages from the channel.')
        # Moderation Commands
        if message.content.startswith('>purge'):
            if client.user.permissions_in(message.channel).manage_messages and client.user.permissions_in(message.channel).read_message_history:
                async for message in client.logs_from(message.channel, limit=int(message.content[7:])+1):
                    await client.delete_message(message)
        
client.run(token, bot=False)
