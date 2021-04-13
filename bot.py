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
stalker = False

MUDAE_ID = 432610292342587392
VARUN_ID = 433045180363309057

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(cxt):
    global name
    global MUDAE_ID
   
    await bot.process_commands(cxt)
    if cxt.author.id == MUDAE_ID:
        if cxt.embeds:
            embed = cxt.embeds[0]
            desc = embed.description
            if embed.author.name == name:
                return
            print(embed.author.name)
            print(embed)
            name = embed.author.name
            # await cxt.channel.send(name)
            return
    if stalker:
        if cxt.author.id == 655167242287317024:
            await cxt.send("^ This man needs help")


@bot.command(description='spits out a preformatted $im command for the last rolled character.')
async def im(cxt):
    string = "$im " + name
    await cxt.send(string)


@bot.command(description='is nas single?')
async def nas(cxt):
    if dating:
        await cxt.send("Nas is single. Big surprise.")
    else:
        await cxt.send("Nas is in a relationship??? What a development.")


@bot.command(description='a summoning command.')
async def campus(cxt):
    await cxt.send("<@655167242287317024> Come to campus?")


@bot.command(aliases=['nastime'], description='set when nas is coming to campus today')
async def nascomin(cxt, arg):
    global campustime
    global nastime

    current_local = time.localtime()
    campustime = int(arg)
    nastime = current_local.tm_mday

    if campustime > 0:
        await cxt.send("Nas time at " + str(campustime) + " :beer:")


@bot.command(aliases=['isnascoming'], description='is nas coming to campus today?')
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


@bot.command(description=':(')
async def nasnotcoming(cxt):
    global campustime

    campustime = 0
    await cxt.send("<:nassmoulder:823289074227085332>")


@bot.command(description='outputs my source on github.')
async def source(cxt):
    embed = discord.Embed()
    embed.description = "[varunkamath/fasir on gh](https://github.com/varunkama)$"
    await cxt.send(embed=embed)


@bot.command(description='I am Abomination.')
async def say(cxt, arg):
    if cxt.author.id == VARUN_ID:
        channel = bot.get_channel(821464624607133726)
        await channel.send(arg)

@bot.command(description='......')
async def stalk(cxt):
    global stalker
    if cxt.author.id == 433045180363309057:
        stalker = not stalker
    else:
        await cxt.send("Sorry man, you're not on the list.")


bot.run(TOKEN)
