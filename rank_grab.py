import random
import markovify

import discord
from discord.ext.commands import UserConverter
# from dotenv import dotenv_values
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from numpy import loadtxt

import itertools

from random import seed
from random import randint
from random import sample

# import requests
from urllib.request import urlopen
import requests
import json


def getJSON(platform, username):
    key = "2cfcd1f6-58bd-466b-9f15-8a41a086cd77"
    headers = { "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0" }
    url = ("https://api.tracker.gg/api/v2/rocket-league/standard/profile/"+"xbl"+"/"+username+"?")
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

def getSummary(platform, username):
    jsonResponse = getJSON(platform, username)
    if not 'results' in jsonResponse or len(jsonResponse['data']) == 0:
        print("OOPS")
    stuff = {}
    for x in range(10):
        try: stuff[jsonResponse["data"]["segments"][x]["metadata"]["name"]] = jsonResponse["data"]["segments"][x]["stats"]["tier"]["metadata"]["name"]
        except: None
    return stuff


def getMMRSum(platform, username):
    jsonResponse = getJSON(platform, username)
    stuff = {}
    for x in range(10):
        try: stuff[jsonResponse["data"]["segments"][x]["metadata"]["name"]] = jsonResponse["data"]["segments"][x]["stats"]["rating"]["value"]
        except: None
    return stuff


def getRank(platform, username, mode):
    jsonResponse = getSummary(platform, username)

    translation = {"1": "Ranked Duel 1v1", "2": "Ranked Doubles 2v2", "3": "Ranked Standard 3v3", "hoops": "Hoops", "rumble": "Rumble", "dropshot": "Dropshot", "snowday": "Snowday", "tournament": "Tournament Matches", "unranked": "Un-Ranked"}
    print(jsonResponse)
    return jsonResponse[translation[mode.lower()]]


def getMMR(platform, username, mode):
    jsonResponse = getMMRSum(platform, username)

    translation = {"1": "Ranked Duel 1v1", "2": "Ranked Doubles 2v2", "3": "Ranked Standard 3v3", "hoops": "Hoops", "rumble": "Rumble", "dropshot": "Dropshot", "snowday": "Snowday", "tournament": "Tournament Matches", "unranked": "Un-Ranked"}
    print(jsonResponse)
    return jsonResponse[translation[mode.lower()]]


if __name__ == "__main__":
    platform = "epic"
    username = "sparetoad813"
    url = ("https://api.tracker.gg/api/v2/rocket-league/standard/profile/"+platform+"/"+username+"?/segments/playlist?season=17")
    
    print(getRank(platform, username, "1"))
    print(getMMR(platform, username, "1"))


    