from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}샌디':
        await message.channel.send("아이도루다요!")

    if message.content.startswith(f'{PREFIX}가챠'):
        await message.channel.send('샌디~~~빔!')
        
    if message.content.startswith(f'{PREFIX}바보'):
        await message.channel.send('바~~~~~~~보!')
        
    if message.content.startswith(f'{PREFIX}안녕'):
        await message.channel.send('@' + message.author.name + ' 아소~봉!')
        
    if message.content.startswith(f'{PREFIX}앨범'):
        await message.channel.send('https://www.youtube.com/watch?v=cKmhab15cCc')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
