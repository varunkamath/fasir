# bot.py
import random
import markovify

import discord
from discord.ext.commands import UserConverter
from dotenv import dotenv_values
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from numpy import loadtxt

import itertools

from random import seed
from random import randint
from random import sample

intents = discord.Intents.default()
intents.members = True

description = '''I AM FASIR'''

help_command = commands.DefaultHelpCommand(no_category='Commands', aliases=['fasir', 'fh', 'fasirhelp'])

bot = commands.Bot(command_prefix='&', description=description, intents=intents, help_command=help_command)
name = "test"
dating = 1
campustime = 0

stalker = False
target = 'nas'
react = False
grrr = False
onetruenas = False

quotefile = "quotes.dat"
seed(1)

config = dotenv_values()
TOKEN = config['DISCORD_TOKEN']
GUILD_ID = int(config['GUILD_ID'])
IDS = dict(itertools.islice(config.items(), 2, None))


def get_id(person):
    if person in IDS:
        print('Key Found')
        print("ID of " + person + ": " + IDS.get(person))
        return int(IDS.get(person))
    else:
        print('Key not found')
        return 0


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(cxt):
    global GUILD_ID

    global name

    global react
    global stalker
    global grrr
    global onetruenas

    await bot.process_commands(cxt)
    if cxt.author.id == get_id('MUDAE'):
        if cxt.embeds:
            embed = cxt.embeds[0]
            if embed.author.name == name:
                return
            print(embed.author.name)
            print(embed)
            name = embed.author.name
    if cxt.author.id == get_id('BOTCHOU'):
        emoji = '<:monchou:823224837438439424>'
        await cxt.add_reaction(emoji)
        emoji = '<:monchouupset:826574963166150696>'
        await cxt.add_reaction(emoji)

    if grrr is True:
        if cxt.content.startswith('&grrr') or cxt.content.startswith('$wa'):
            return
        else:
            grrr = False
            guild = bot.get_guild(GUILD_ID)
            emojis = sample(guild.emojis, 20)

            for emoji in emojis:
                await cxt.add_reaction(emoji)

    if react:
        if cxt.content.startswith('&react') or cxt.content.startswith('$wa'):
            return
        else:
            react = False
            emoji = '<:naslook:823289042389041182>'
            await cxt.add_reaction(emoji)

    if stalker:

        if target.lower() == 'nas' and cxt.author.id == get_id('NAS'):
            emoji = '<:naslook:823289042389041182>'
            await cxt.add_reaction(emoji)
            channel = cxt.channel
            await channel.send("^ This man needs help")
        if target.lower() == 'mckeever' and cxt.author.id == get_id('MCKEEVER'):
            emoji = '<:carsondoubt:821429229303627798>'
            await cxt.add_reaction(emoji)
            channel = cxt.channel
            await channel.send("Your bot isn't as good as me.")
        if target.lower() == 'brody' and cxt.author.id == get_id('BRODY'):
            emoji = '<:brodysad:818335942346670091>'
            await cxt.add_reaction(emoji)
            channel = cxt.channel
        if target.lower() == 'jay' and cxt.author.id == get_id('JAY'):
            emoji = '<:jasonangry:821109068457705522> '
            await cxt.add_reaction(emoji)
            channel = cxt.channel
            await channel.send("You'll never get Emilia.")
        if target.lower() == 'geesh' and cxt.author.id == get_id('GEESH'):
            emoji = '<:Geeshshrouded:826574963901071370>'
            await cxt.add_reaction(emoji)
            channel = cxt.channel
            await channel.send("Get off TikTok.")

    if cxt.guild is None and cxt.author != bot.user and cxt.author.id != get_id('VARUN'):
        guild = bot.get_guild(GUILD_ID)
        channel = discord.utils.get(guild.channels, name="bot-testing")
        message = cxt.author.name + " just sent me this message: " + cxt.content
        await channel.send(message)

    if onetruenas:
        if cxt.author.id == get_id('NAS') and not cxt.content.startswith('&onetruenas'):
            text = cxt.content
            await cxt.delete()
            await cxt.channel.send(text)


@bot.event
async def on_command_error(cxt, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


@bot.command(aliases=['fh', 'fasir'], brief='Fasir-specific &help.')
async def fasirhelp(cxt):
    await cxt.send_help()


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

    campustime = int(arg)

    if campustime > 0:
        await cxt.send("Nas time at " + str(campustime) + " :beer:")


@bot.command(aliases=['isnascoming'], brief='Is nas coming to campus today?')
async def isnascomin(cxt):
    global campustime
    string = "Nas isn't coming today :("

    if campustime > 0:
        string = "Nas is coming to campus at " + str(campustime)
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
    if (cxt.author.id == get_id('VARUN') or cxt.author.id == get_id('NAS')) and chan is None:
        channel = bot.get_channel(821464624607133726)
        await channel.send(arg)
        await cxt.message.add_reaction('<:naslook:823289042389041182>')
    elif cxt.author.id == get_id('VARUN') or cxt.author.id == get_id('NAS'):
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
async def stalk(cxt, person=None):
    global stalker
    global target

    if cxt.author.id == get_id('VARUN'):
        if stalker:
            await cxt.send(":)")
        else:
            await cxt.send(">:)")
        target = person
        stalker = not stalker
    else:
        await cxt.send("Sorry man, you're not on the list.")


@bot.command(brief='React to the next message.')
async def react(cxt):
    global react
    react = True


@bot.command(aliases=['aq'], brief='Add a nas quote.')
async def addquote(cxt, *, new):
    global quotefile

    if new.startswith('\"') and new.endswith('\"'):
        new = new[1:-1]
    if new.startswith('\'') and new.endswith('\''):
        new = new[1:-1]

    if "\n" in new:
        new.replace("\n", " ")

    entry = "\n\'" + new + "\'"

    file = open(quotefile, "a")
    file.write(entry)
    file.close()

    await cxt.message.add_reaction('<:nasstoic:823289074227085332>')


@bot.command(aliases=['rq', 'r'], brief='Remove last quote.')
async def removequote(cxt):
    global quotefile

    msgs = []
    async for message in cxt.channel.history(limit=100):
        if message.author.id == get_id('FASIR') and message.content.endswith(" - Nasir Nourkadi"):
            msgs.append(message.content)
            break

    message = msgs[0]
    quote = message.split("' -", 1)
    quote = quote[0] + "'"

    with open(quotefile, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i.strip("\n") != quote:
                f.write(i)
        f.truncate()

    await cxt.message.add_reaction('<:nasstoic:823289074227085332>')


@bot.command(aliases=['nq', 'q', 'quote'], brief='What would nas say in this situation?')
async def nasquote(cxt):
    global quotefile

    quotes = loadtxt(quotefile, comments="#", delimiter="\n", unpack=False, dtype=str)
    num = randint(0, len(quotes) - 1)
    random.shuffle(quotes)
    quote = quotes[num] + " - Nasir Nourkadi"

    await cxt.send(quote)


@bot.command(aliases=['gnq', 'gq', 'gquote'], brief='What would fas say in this situation?')
async def generatenasquote(cxt):
    global quotefile

    # Get raw text as string.
    with open(quotefile) as f:
        text = f.read()
    # Build the model.
    text_model = markovify.NewlineText(text, state_size=1, well_formed=False)
    # Print five randomly-generated sentences
    generated_quote = text_model.make_sentence()
    stripped_quote = generated_quote[1:-1]
    quote = generated_quote + " - Fasir Fourkadi"

    await cxt.send(quote)


@bot.command(pass_context=True, brief='Make whoever sends the next message feel like Kanye.')
async def grrr(cxt):
    global grrr
    grrr = True
    await cxt.message.delete()
    # global GUILD_ID
    # guild = bot.get_guild(GUILD_ID)
    # emojis = sample(guild.emojis, 20)
    #
    # for emoji in emojis:
    #     await cxt.message.add_reaction(emoji)


@bot.command(pass_context=True, brief='Clear your last x messages in the channel.')
async def clear(cxt, n=None, user=None, user2=None):
    if n is None:
        await cxt.send("Use &clear to clear the last few messages in the channel. Usage: \'&clear 5\' will clear your "
                       "last 5 messages, and \'&clear 5 all\' will clear the last 5 messages by any user.")
        return

    msgs = []
    msg1 = []
    msg2 = []
    number = int(n)
    everyone = False

    if user is None:
        user_id = cxt.author.id
    elif user2 is None and user.lower() != 'all':
        user_id = get_id(user.upper())
    elif user.lower() == 'all':
        everyone = True
    else:
        user_id = get_id(user.upper())
        user2_id = get_id(user2.upper())

    msgs.append(cxt.message)

    if everyone is True:
        async for message in cxt.channel.history(limit=100):
            if message.id != cxt.message.id and len(msg1) < number:
                msg1.append(message)
        msgs = msgs + msg1
    else:
        async for message in cxt.channel.history(limit=100):
            if message.id != cxt.message.id and len(msg1) < number and message.author.id == user_id:
                msg1.append(message)
            if user2 is None:
                pass
            else:
                if message.id != cxt.message.id and len(msg2) < number and message.author.id == user2_id:
                    msg2.append(message)
        msgs = msgs + msg1 + msg2

    await cxt.channel.delete_messages(msgs)


@bot.command(pass_context=True, brief='There can only be one.')
async def onetruenas(cxt):
    global onetruenas
    if cxt.author.id == get_id('VARUN') and onetruenas:
        onetruenas = not onetruenas
        print(onetruenas)
        await cxt.send("There can be two.")
    elif cxt.author.id == get_id('VARUN'):
        onetruenas = not onetruenas
        print(onetruenas)
        await cxt.send("THERE CAN ONLY BE ONE.")
    else:
        await cxt.send("Sorry man, you're not on the list.")


bot.run(TOKEN)
