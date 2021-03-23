# bot.py
import os
import time

import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

description = '''I AM FASIR'''

initial_local = time.localtime()

bot = commands.Bot(command_prefix='&', description=description, intents=intents)
name = "test"
dating = 1
campustime = 0
nastime = initial_local.tm_mday

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# @bot.event
# async def on_message()
#

@bot.event
async def on_message(cxt):
    global name

    await bot.process_commands(cxt)
    if cxt.author.id == 432610292342587392:
        if cxt.embeds:
            embed = cxt.embeds[0]
            if embed.author.name == name:
                return
            print(embed.author.name)
            name = embed.author.name
            # await cxt.channel.send(name)
            return

@bot.command()
async def im(cxt):
    string = "$im " + name
    await cxt.send(string)

@bot.command()
async def nas(cxt):
    if dating:
        await cxt.send("Nas is single. Big surprise.")
    else:
        await cxt.send("Nas is in a relationship??? What a development.")

@bot.command()
async def campus(cxt):
    await cxt.send("<@655167242287317024> Come to campus?")

@bot.command()
async def nascomin(cxt, arg):
    global campustime
    global nastime

    current_local = time.localtime()
    campustime = int(arg)
    nastime = current_local.tm_mday

    if campustime > 0:
        await cxt.send("Nas time at " + str(campustime) + " :beer:")

@bot.command()
async def nastime(cxt, arg):
    global campustime
    global nastime

    current_local = time.localtime()
    campustime = int(arg)
    nastime = current_local.tm_mday

    if campustime > 0:
        await cxt.send("Nas time at " + str(campustime) + " :beer:")

@bot.command()
async def isnascomin(cxt):
    global campustime
    global nastime

    current_local = time.localtime()
    print(current_local.tm_mday)

    string = "Nas isn't coming today :("

    if current_local.tm_mday == nastime:
        if campustime > 0:
            string = "Nas is comin to campus at " + str(campustime)
        else:
            string = "Nas isn't coming today :("

    await cxt.send(string)

@bot.command()
async def isnascoming(cxt):
    global campustime
    global nastime

    current_local = time.localtime()
    print(current_local.tm_mday)

    string = "Nas isn't coming today :("

    if current_local.tm_mday == nastime:
        if campustime > 0:
            string = "Nas is comin to campus at " + str(campustime)
        else:
            string = "Nas isn't coming today :("

    await cxt.send(string)

@bot.command()
async def nasnotcoming(cxt):
    global campustime

    campustime = 0
    await cxt.send(":nassmoulder:")

bot.run(TOKEN)
