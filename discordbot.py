from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
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
        await message.channel.send('@{}'.format(message.author.name) + ' 아소~봉!')
        
    if message.content.startswith(f'{PREFIX}앨범'):
        await message.channel.send('https://www.youtube.com/watch?v=cKmhab15cCc')
@bot.command
async def game(ctx, user: str):  # user:str로 !game 다음에 나오는 메시지를 받아줌
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot)  # 인덱스 비교로 결과 결정
    if result == 0:
        await ctx.send(f'{user} vs {bot}  비겼습니다.')
    elif result == 1 or result == -2:
        await ctx.send(f'{user} vs {bot}  유저가 이겼습니다.')
    else:
        await ctx.send(f'{user} vs {bot}  봇이 이겼습니다.')
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
