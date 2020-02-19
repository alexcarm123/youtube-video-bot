
import os
import random
import csv

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='babish')
async def babish_videos(ctx):
    f=csv.DictReader(open('Babish_Videos.csv','r'))
    vids=[]

    for row in f:
        vids.append(row['Videos'])

    response = random.choice(vids)
    await ctx.send(response)
#@client.event
#async def on_ready():
    #print(f'{client.user} has connected to Discord!')
    
bot.run(TOKEN)