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
    args = message.content.split(' | ')
    if message.author.id == client.user.id:
        # General Commands
        if args[0] == '>help':
            await client.send_message(message.channel, '**Commands List:**\n`>help` - sends this message. Lists all commands.\n`>purge [x]` - deletes x messages from the channel.')
        # Moderation Commands
        if args[0] == '>purge':
            if client.user.permissions_in(message.channel).manage_messages and client.user.permissions_in(message.channel).read_message_history:
                async for message in client.logs_from(message.channel, limit=int(args[1])+1):
                    await client.delete_message(message)
        if args[0] == '>kick':
            if client.user.permissions_in(message.channel).kick_users:
                await client.kick(message.mentions[0])
                print("Kicked user "+message.mentions[0]+" from server "+message.server)
        if args[0] == '>ban':
            if client.user.permissions_in(message.channel).ban_users:
                await client.ban(message.mentions[0])
                print("Banned user "+message.mentions[0]+" from server "+message.server)
        
client.run(token, bot=False)
