import discord
import asyncio

token = ""
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("-----")

    await client.change_presence(game=discord.Game(name="Discord.py"))

@client.event
async def on_message(message):
    if message.author.id == '224712063832948736':
        if message.content.startswith('>help'):
            await client.send_message(message.channel, '**Commands List:**\n`>help` - sends this message. Lists all commands.')

client.run(token, bot=False)
