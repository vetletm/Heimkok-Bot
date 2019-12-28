#!/usr/bin/env python3

import os
import logging

from discord.ext import commands

from bot_commands import BotCommands

# Set up logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up bot
bot = commands.Bot(command_prefix='!',
                   description='Heimkok is a simple bot for simple stuff')

# Attempt to get the BOT_TOKEN
BOT_TOKEN = None
try:
    BOT_TOKEN = os.environ['BOT_TOKEN']
    logger.info('Sucessfully imported BOT_TOKEN')
except Exception as error:
    logger.critical('Could not import BOT_TOKEN, error: %s', error)
    exit(1)

if not BOT_TOKEN:
    logger.critical('Fetching BOT_TOKEN failed without exception, exiting')
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
    try:
        response = command.get_joke('norris')
        await ctx.send(response)
        logger.info('Fetched and returned joke of type norris')
    except Exception as error:
        logger.warning('Could not get joke of type norris, error: %s', error)


@joke.command(name='programming')
async def joke_programming(ctx):
    """ Nerdy jokes
        """
    try:
        response = command.get_joke('programming')
        await ctx.send(response)
        logger.info('Fetched and returned a joke of type programming')
    except Exception as error:
        logger.warning('Could not get joke of type programming, error: %s', error)


@joke.command(name='random')
async def joke_random(ctx):
    """ Random, funny jokes
    """
    try:
        response = command.get_joke('random')
        await ctx.send(response)
        logger.info('Fetched and returned a random joke')
    except Exception as error:
        logger.warning('Could not get joke of random type, error: %s', error)


@commands.cooldown(rate=1, per=1, type=commands.BucketType.default)
@bot.command()
async def weather(ctx, req):
    """ Gives you some information based on your desired city.
    Usage: !weather Oslo (keep it unambiguous)
        """
    try:
        city_request = ''.join(req)
        response = command.get_weather(city_request)
        await ctx.send(response)
        logger.info('Fetched and returned the weather for City %s', city_request)
    except Exception as error:
        logger.warning('Could not get the weather for city: %s, error: %s', city_request, error)


@bot.command()
async def catfact(ctx):
    """ Will provide you with a neat cat fact!
        """
    try:
        response = command.get_catfact()
        await ctx.send(response)
        logger.info('Fetched and returned a catfact')
    except Exception as error:
        logger.warning('Could not fetch catfact, error: %s', error)


@bot.group(invoke_without_command=True)
async def cuteanimal(ctx):
    """ Will provide you with a picture of a cute animal!
        usage: !cuteanimal <some animal> or !cuteanimal
        If the animal you want to see is not in the list, it will return a random picture instead.
        No specified animal will result in a random picture.
    """
    try:
        response = command.get_animal()
        await ctx.send(response)
        logger.info('Fetched and returned a picture of a cute animal')
    except Exception as error:
        logger.warning('Could not fetch a picture of a cute animal, error: %s', error)


@cuteanimal.command(name='cat')
async def cuteanimal_cat(ctx):
    """ returns a cute cat
    """
    try:
        response = command.get_animal('cat')
        await ctx.send(response)
        logger.info('Fetched and returned a picture of a cat')
    except Exception as error:
        logger.warning('Could not fetch cat picture, error: %s', error)


@cuteanimal.command(name='shibe')
async def cuteanimal_shibe(ctx):
    """ returns a cute shiba inu
    """
    try:
        response = command.get_animal('shibe')
        await ctx.send(response)
        logger.info('Fetched and returned a picture of a shiba inu')
    except Exception as error:
        logger.warning('Could not fetch shiba inu picture, error: %s', error)


@cuteanimal.command(name='fox')
async def cuteanimal_fox(ctx):
    """ returns a cute fox
    """
    try:
        response = command.get_animal('fox')
        await ctx.send(response)
        logger.info('Fetched and returned a picture of a fox')
    except Exception as error:
        logger.warning('Could not fetch picture of a fox, error: %s', error)


@cuteanimal.command(name='dog')
async def cuteanimal_dog(ctx):
    """ returns a cute dog
    """
    try:
        response = command.get_animal('dog')
        await ctx.send(response)
        logger.info('Fetched and returned a picture of a dog')
    except Exception as error:
        logger.warning('Could not fetch a picture of a dog, error: %s', error)


@cuteanimal.command(name='dog2')
async def cuteanimal_dog(ctx):
    """ more dogs!
    """
    try:
        response = command.get_animal('dog2')
        await ctx.send(response)
        logger.info('Fetched and returned a picture of a dog2')
    except Exception as error:
        logger.warning('Could not fetch a picture of a dog2, error: %s', error)


@bot.command()
async def eyebleach(ctx):
    """
    Bleach yer eyes!
    """
    response = command.eyebleach('')
    await ctx.send(response)
    logger.info('Fetched and returned a random post')


@bot.event
async def on_ready():
    name = bot.user.name
    logger.info('Logged in as %s and ready to mingle!', name)


try:
    command = BotCommands()
except Exception as error:
    logger.critical('Failed to define command-object, reason: %s', error)
    exit(2)

try:
    bot.run(BOT_TOKEN)
except Exception as error:
    logger.critical('Failed to start bot, error: %s', error)
    exit(3)
