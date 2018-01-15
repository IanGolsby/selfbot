import discord
from discord.ext import commands

token = "MjI0NzEyMDYzODMyOTQ4NzM2.Cree6w.fjA5WKPVuHhXRGAzG5rOmS3CseE"
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("-----")

    await client.change_presence(game=discord.Game(name="Discord.py"))

    idgo = client.user

@client.event
async def on_message(message):
    if message.author.id == '224712063832948736':
        # General Commands
        if message.content.startswith('>help'):
            await client.send_message(message.channel, '**Commands List:**\n`>help` - sends this message. Lists all commands.')
        # Moderation Commands
        if message.content.startswith('>purge'):
            if idgo.permissions_in(message.channel).manage_messages:
                
                
client.run(token, bot=False)
