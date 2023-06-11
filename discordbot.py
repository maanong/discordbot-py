from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    if message.content.startswitch(f'{PREFIX} '):
        keyword = message.content.replace(f'{PREFIX} ', "")
        url = f"https://www.youtube.com/results?search_query={keyword}"

        msg = await message.channel.send(embed=discord.Embed(title="잠시만 기다려주세요!\n정보를 수집 중이므로 다소 시간이 걸릴 수 있습니다.",
                                                             description=f"[ {message.author.mention} ]", color=0xFF9900))

        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.close()

        video_info = soup.find("a", attrs={"id": "video-title"})
        title = video_info.get("title")
        visit = video_info.get("aria-label").split(" ")[-1]
        href = video_info.get("href")

        await msg.delete()
        await message.channel.send(f"**{keyword} 의 검색 결과입니다.**\n\n{title} | 조회수 {visit}\nhttp://youtube.com{href}")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
