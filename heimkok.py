#!/usr/bin/env python3

import os

from discord.ext import commands

from bot_commands import BotCommands

bot = commands.Bot(command_prefix='!', description='Heimkok is a simple bot for simple stuff')

if 'BOT_TOKEN' in os.environ:
    BOT_TOKEN = os.environ['BOT_TOKEN']
else:
    print('BOT_TOKEN must be passed as an environment variable')
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
    response = command.get_joke('norris')
    await ctx.send(response)


@joke.command(name='programming')
async def joke_programming(ctx):
    """ Nerdy jokes
        """
    response = command.get_joke('programming')
    await ctx.send(response)


@joke.command(name='random')
async def joke_random(ctx):
    """ Random, funny jokes
    """
    response = command.get_joke('random')
    await ctx.send(response)


@commands.cooldown(rate=1, per=1, type=commands.BucketType.default)
@bot.command()
async def weather(ctx, req):
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
    response = command.get_catfact()
    await ctx.send(response)


@bot.group(invoke_without_command=True)
async def cuteanimal(ctx):
    """ Will provide you with a picture of a cute animal!
        usage: !cuteanimal <some animal> or !cuteanimal
        If the animal you want to see is not in the list, it will return a random picture instead.
        No specified animal will result in a random picture.
    """
    response = command.get_animal()
    await ctx.send(response)


@cuteanimal.command(name='cat')
async def cuteanimal_cat(ctx):
    """ returns a cute cat
    """
    response = command.get_animal('cat')
    await ctx.send(response)


@cuteanimal.command(name='shibe')
async def cuteanimal_shibe(ctx):
    """ returns a cute shiba inu
    """
    response = command.get_animal('shibe')
    await ctx.send(response)


@cuteanimal.command(name='fox')
async def cuteanimal_fox(ctx):
    """ returns a cute fox
    """
    response = command.get_animal('fox')
    await ctx.send(response)


@cuteanimal.command(name='dog')
async def cuteanimal_dog(ctx):
    """ returns a cute dog
    """
    response = command.get_animal('dog')
    await ctx.send(response)


@cuteanimal.command(name='dog2')
async def cuteanimal_dog(ctx):
    """ more dogs!
    """
    response = command.get_animal('dog2')
    await ctx.send(response)


@bot.event
async def on_ready():
    name = bot.user.name
    print('Logged in as %s and ready to mingle!' % name)


command = BotCommands()

bot.run(BOT_TOKEN)
