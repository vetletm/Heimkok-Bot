#!/usr/bin/env python3

# Heimkok is a simple bot for simple stuff. Cute pics of animals and later:
#   Interacting with Wunderlist
# TODO: Add Wunderlist functionality
# TODO: Add imagescraper functionality
# TODO: Add better jokes functionality
# TODO: Add Postgres for jokes, animals, and weather

import discord, requests, random, sys, json, time
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Heimkok is a simple bot for simple stuff')

if len(sys.argv) > 2:
    BOT_TOKEN = sys.argv[1]
    WEATHER_API_TOKEN = sys.argv[2]
else:
    print('Usage: heimkok.py <BOT_TOKEN> <WEATHER_API_TOKEN>')
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
            animal = self.animals[str(r % mod)]
        elif kind:
            # Find the specific animal by (very inefficiently) iterating through the jsonfile
            for i in self.animals:
                if kind == self.animals[i]['animal']:
                    animal = self.animals[i]
                    break

        # Attempt to fetch the direct link to the animal picture
        try:
            resp = requests.get(animal['url'])
        except requests.exceptions.HTTPError as e:
            return 'Could not fetch cute pic, sorry. Reason: ' + str(e)
        return resp.json()[animal['file']]

    # Returns a neat cat fact
    def fetch_catfact(self):
        resp = requests.get('https://cat-fact.herokuapp.com/facts/random')
        return resp.json()['text']

'''
This class uses the OpenWeatherMap API, free edition.
'''
class WeatherStorage:
    def __init__(self):
        self.prefix = 'https://api.openweathermap.org/data/2.5/weather?q='
        self.suffix = '&units=metric'
        self.appid = '&appid=' + WEATHER_API_TOKEN

    def fetch_weather(self, city):
        weather_url = ''.join([self.prefix,city,self.suffix,self.appid])
        resp = requests.get(weather_url)

        # Craft a neat response on the form:
        '''
        City: Oslo
        Temperature: 3.58℃
        Description: shower rain
        Wind: 5.7m/s, direction: N
        '''
        temp    = "Temperature: " + str(resp.json()['main']['temp']) + chr(8451)
        loc     = "City: " + str(resp.json()['name'])
        descr   = "Description: " + resp.json()['weather'][0]['description']
        winddir = self.degrees_to_cardinal(resp.json()['wind']['deg'])
        wind    = "Wind: " + str(resp.json()['wind']['speed']) + 'm/s' + ', direction: ' + str(winddir)

        forecast = '\n'.join([loc,temp,descr,wind])

        return forecast

    # Kudos to https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f for this:
    def degrees_to_cardinal(self,d):
        '''
        note: this is highly approximate...
        '''
        dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        ix = int((d + 11.25)/22.5)
        return dirs[ix % 16]


def fetch_joke():
    # TODO: Expand to accept arguments to return different types of jokes
    resp = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
    data = resp.json()[0]
    joke = data['setup'] + ' || ' + data['punchline'] + ' ||'
    return joke


@bot.command()
async def joke(ctx):
    """ Returns a dad-joke of exceptional calibre!
        """
    await ctx.send(fetch_joke())


@commands.cooldown(rate=1,per=1,type=commands.BucketType.default)
@bot.command()
async def weather(ctx,req):
    """ Not implemented, it's always fine weather.
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


@bot.event
async def on_ready():
    name = bot.user.name
    print('Logged in as %s and ready to mingle!' % name)


animal  = AnimalStorage()
weather = WeatherStorage()

bot.run(BOT_TOKEN)
