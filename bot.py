# bot.py
import os
import time

import discord
from discord.ext.commands import UserConverter
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

description = '''I AM FASIR'''

initial_local = time.localtime()

help_command = commands.DefaultHelpCommand(no_category='Commands')

bot = commands.Bot(command_prefix='&', description=description, intents=intents, help_command=help_command)
name = "test"
dating = 1
campustime = 0
nastime = initial_local.tm_mday
stalker = False
react = False

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
    global react

    await bot.process_commands(cxt)
    if cxt.author.id == MUDAE_ID:
        if cxt.embeds:
            embed = cxt.embeds[0]
            if embed.author.name == name:
                return
            print(embed.author.name)
            print(embed)
            name = embed.author.name
            return
    if cxt.author.id == 822551143166509074:
        emoji = '<:monchou:823224837438439424>'
        await cxt.add_reaction(emoji)
        emoji = '<:monchouupset:826574963166150696>'
        await cxt.add_reaction(emoji)

    if react:
        if cxt.content.startswith('&react') or cxt.content.startswith('$wa'):
            return
        else:
            emoji = '<:naslook:823289042389041182>'
            await cxt.add_reaction(emoji)
            react = False

    if stalker:
        if cxt.author.id == 655167242287317024:
            emoji = '<:naslook:823289042389041182>'
            await cxt.add_reaction(emoji)
            channel = cxt.channel
            await channel.send("^ This man needs help")
        if cxt.author.id == 510544762953138177:
            emoji = '<:carsondoubt:821429229303627798>'
            await cxt.add_reaction(emoji)
            channel = cxt.channel
            await channel.send("Your bot isn't as good as me.")
        if cxt.author.id == 400130051078750218:
            emoji = '<:brodysad:818335942346670091>'
            await cxt.add_reaction(emoji)
            channel = cxt.channel
            await channel.send("You got a cute dog. Kinda racist, though.")

    if cxt.guild is None and cxt.author != bot.user and cxt.author.id != 433045180363309057:
        guild = bot.get_guild(817230167063527455)
        channel = discord.utils.get(guild.channels, name="bot-testing")
        message = cxt.author.name + " just sent me this message: " + cxt.content
        await channel.send(message)


@bot.command(brief='Spits out a preformatted $im command for the last rolled char.')
async def im(cxt):
    string = "$im " + name
    await cxt.send(string)


@bot.command(brief='Is nas single?')
async def nas(cxt):
    if dating:
        await cxt.send("Nas is single. Big surprise.")
    else:
        await cxt.send("Nas is in a relationship??? What a development.")


@bot.command(brief='A summoning command.')
async def campus(cxt):
    await cxt.send("<@655167242287317024> Come to campus?")


@bot.command(aliases=['nastime'], brief='Set when nas is coming to campus today')
async def nascomin(cxt, arg):
    global campustime
    global nastime

    current_local = time.localtime()
    campustime = int(arg)
    nastime = current_local.tm_mday

    if campustime > 0:
        await cxt.send("Nas time at " + str(campustime) + " :beer:")


@bot.command(aliases=['isnascoming'], brief='Is nas coming to campus today?')
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


@bot.command(brief=':(')
async def nasnotcoming(cxt):
    global campustime

    campustime = 0
    await cxt.send("<:nassmoulder:823289074227085332>")


@bot.command(brief='Outputs my source on github.')
async def source(cxt):
    embed = discord.Embed()
    embed.description = "[varunkamath/fasir on gh](https://github.com/varunkamath/fasir)"
    await cxt.send(embed=embed)


@bot.command(aliases=['s'], brief='I am Abomination.')
async def say(cxt, arg, chan=None):
    if cxt.author.id == VARUN_ID and chan is None:
        channel = bot.get_channel(821464624607133726)
        await channel.send(arg)
        await cxt.add_reaction('<:naslook:823289042389041182>')
    elif cxt.author.id == VARUN_ID:
        channel = discord.utils.get(cxt.guild.channels, name=chan)
        await channel.send(arg)
        await cxt.message.add_reaction('<:naslook:823289042389041182>')
    else:
        await cxt.send("I am beholden only to <@433045180363309057>.")


@bot.command(aliases=['w'], brief='Whisper to someone.')
async def whisper(cxt, message, person):
    converter = UserConverter()
    user = await converter.convert(cxt, person)
    await user.send(message)
    await cxt.message.add_reaction('<:naslook:823289042389041182>')


@bot.command(brief='......')
async def stalk(cxt):
    global stalker
    if cxt.author.id == 433045180363309057:
        if stalker:
            await cxt.send(":)")
        else:
            await cxt.send(">:)")
        stalker = not stalker
    else:
        await cxt.send("Sorry man, you're not on the list.")


@bot.command(brief='React to the next message.')
async def react(cxt):
    global react
    react = True


bot.run(TOKEN)
