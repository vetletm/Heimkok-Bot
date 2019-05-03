#!/usr/bin/env python3

import discord, sys
from discord.ext import commands

import weather as w
import jokes as j
import animals as a

bot = commands.Bot(command_prefix='!', description='Heimkok is a simple bot for simple stuff')

# TODO: Update to use argparse, because this just ain't no fucking good at all
if len(sys.argv) > 2:
    BOT_TOKEN = sys.argv[1]
else:
    print('Usage: heimkok.py <BOT_TOKEN> <WEATHER_API_TOKEN>')
    exit(1)


@bot.group(invoke_without_command=False)
async def joke(ctx):
    """ Must be used with a desired type of joke:
        Chuck Norris, Programming, or Random.
        usage: !joke norris
        """
    pass

@joke.command(name='norris')
async def joke_norris(ctx):
    """ A kick-ass Chuck Norris joke!
        """
    response = jokes.fetch_joke_norris()
    await ctx.send(response)

@joke.command(name='programming')
async def joke_programming(ctx):
    """ Nerdy jokes
        """
    response = jokes.fetch_joke_programming()
    await ctx.send(response)

@joke.command(name='random')
async def joke_random(ctx):
    """ Random, funny jokes
        """
    response = jokes.fetch_joke_random()
    await ctx.send(response)


@commands.cooldown(rate=1,per=1,type=commands.BucketType.default)
@bot.command()
async def weather(ctx,req):
    """ Gives you some information based on your desired city.
    Usage: !weather Oslo (keep it unambiguous)
        """
    city_request = ''.join(req)
    response = weather.fetch_weather(city_request)
    await ctx.send(response)


@bot.command()
async def catfact(ctx):
    """ Will provide you with a neat cat fact!
        """
    response = animal.fetch_catfact()
    await ctx.send(response)


@bot.group(invoke_without_command=True)
async def cuteanimal(ctx):
    """ Will provide you with a picture of a cute animal!
        usage: !cuteanimal <some animal> or !cuteanimal
        If the animal you want to see is not in the list, it will return a random picture instead.
        No specified animal will result in a random picture.
    """
    response = animal.fetch_animalpic('')
    await ctx.send(response)

@cuteanimal.command(name='cat')
async def cuteanimal_cat(ctx):
    """ returns a cute cat
    """
    response = animal.fetch_animalpic('cat')
    await ctx.send(response)

@cuteanimal.command(name='shibe')
async def cuteanimal_shibe(ctx):
    """ returns a cute shiba inu
    """
    response = animal.fetch_animalpic('shibe')
    await ctx.send(response)

@cuteanimal.command(name='fox')
async def cuteanimal_fox(ctx):
    """ returns a cute fox
    """
    response = animal.fetch_animalpic('fox')
    await ctx.send(response)

@cuteanimal.command(name='dog')
async def cuteanimal_dog(ctx):
    """ returns a cute dog
    """
    response = animal.fetch_animalpic('dog')
    await ctx.send(response)

@cuteanimal.command(name='dog2')
async def cuteanimal_dog(ctx):
    """ more dogs!
    """
    response = animal.fetch_animalpic('dog2')
    await ctx.send(response)


@bot.event
async def on_ready():
    name = bot.user.name
    print('Logged in as %s and ready to mingle!' % name)


animal  = a.Animals()
weather = w.Weather()
jokes = j.Jokes()

bot.run(BOT_TOKEN)
