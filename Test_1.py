
import os
import random
import csv

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='fails')
async def babish_videos(ctx):
    f=csv.DictReader(open('Videos.csv','r'))
    vids=[]

    for row in f:
        vids.append(row['Link'])

    response = random.choice(vids)
    await ctx.send(response)
#@bot.event
#async def on_ready():
    #print(f'{bot.user} has connected to Discord!')
    
bot.run(TOKEN)