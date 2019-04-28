# Heimkok is a simple bot for simple stuff. Cute pics of animals and later:
#   Interacting with Wunderlist
# TODO: Add Wunderlist functionality
# TODO: Add imagescraper functionality
# TODO: Add better jokes functionality
# TODO: Add Postgres for jokes, animals, and weather

import discord, requests, random, sys, json, time
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
        # Reads jsonfile with all animals
        with open('animals.json','r') as f:
            self.animals = json.loads(f.read())

    def fetch_animalpic(self,kind):
        # Either random or specific, based on !cuteanimal or !cuteanimal <animal>
        if not kind:
            mod = len(self.animals)
            r = random.randint(1, 1000)
            a = self.animals[str(r % mod)]
        elif kind:
            # Find the specific animal by (very inefficiently) iterating through the jsonfile
            for i in range(len(self.animals)):
                if kind == self.animals[str(i)]['animal']:
                    a = self.animals[str(i)]
                    break

        # Attempt to fetch the direct link to the animal picture
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


@bot.event
async def on_ready():
    name = bot.user.name
    print('Logged in as %s and ready to mingle!' % name)


bot.run(token)
