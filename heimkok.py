# Heimkok is a simple bot for simple stuff. Cute pics of animals and later:
#   Interacting with Wunderlist
# TODO: Add Wunderlist functionality
# TODO: Add imagescraper functionality

import discord, requests, random, sys
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Heimkok is a simple bot for simple stuff')

if len(sys.argv) > 1:
    token = sys.argv[1]
else:
    print('Usage: heimkok.py <token>')
    exit(1)


class AnimalStorage:
    # Animal dictionary to fetch a random animal picture
    def __init__(self):
        self.animals = {
        '0': {
            'animal': 'shibe',
            'url': 'http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true',
            'file': 0
        },
        '1': {
            'animal': 'cat',
            'url': 'https://aws.random.cat/meow',
            'file': 'file'
            },
        '2': {
            'animal': 'fox',
            'url': 'https://randomfox.ca/floof/',
            'file': 'image'
        },
    }

    # Returns either a cat, a shibe, or a fox.
    def fetch_animalpic(self,kind):
        # Set r to be random, mod is how many animals in animals-dict, animal is a random id to use for requests
        mod = len(self.animals)
        if not kind:
            r = random.randint(1, 1000)
            a = self.animals[str(r % mod)]
        elif int(kind) < len(self.animals):
            a = self.animals[kind]
        else:
            return 'Could not fetch cute pic, sorry.'

        try:
            resp = requests.get(a['url'])
        except requests.exceptions.HTTPError as e:
            return 'Could not fetch cute pic, sorry. Reason: ' + str(e)
        return resp.json()[a['file']]

    # Returns a neat cat fact
    def fetch_catfact(self):
        resp = requests.get('https://cat-fact.herokuapp.com/facts/random')
        return resp.json()['text']


animal = AnimalStorage()


def fetch_joke():
    # TODO: Expand to accept arguments to return different types of jokes
    resp = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
    data = resp.json()[0]
    joke = data['setup'] + ' || ' + data['punchline'] + ' ||'
    return joke


# Ideally returns weather in passed city + country code
def fetch_weather():
    # TODO: Find a good Weather API
    resp = 'weather is fine'
    return resp


@bot.command()
async def joke(ctx):
    """ Returns a dad-joke of exceptional calibre!
        """
    await ctx.send(fetch_joke())


@bot.command()
async def weather(ctx):
    """ Not implemented, it's always fine weather.
        """
    await ctx.send(fetch_weather())


@bot.command()
async def catfact(ctx):
    """ Will provide you with a neat cat fact!
        """
    response = animal.fetch_catfact()
    await ctx.send(response)


@bot.command()
async def cuteanimal(ctx,*kind):
    """ Will provide you with a picture of a cute animal!
        usage: !cuteanimal <id of animal {0-2} >
        animals: shibe = 0, cat = 1, fox = 2
        If you only call !cuteanimal, you will randomly get either a fox, a shibe, or a cat.
    """
    response = animal.fetch_animalpic(''.join(kind))
    await ctx.send(response)


@bot.event
async def on_ready():
    name = bot.user.name
    print('Logged in as %s and ready to mingle!' % name)


bot.run(token)
