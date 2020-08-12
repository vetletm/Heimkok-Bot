from commands.animals import Animals
from commands.covid import Covid
from commands.jokes import Jokes
from commands.weather import Weather


class BotCommands:
    """
    Wrapper class for all functionality
    """

    def __init__(self):
        self.weather = Weather()
        self.animals = Animals()
        self.jokes = Jokes()
        self.covid = Covid()

    def get_weather(self, city):
        return self.weather.fetch_weather(city)

    def get_animal(self, kind: str = ''):
        return self.animals.fetch_animalpic(kind)

    def get_catfact(self):
        return self.animals.fetch_catfact()

    def get_joke(self, joke_type):
        if joke_type == 'programming':
            return self.jokes.fetch_joke_programming()
        if joke_type == 'norris':
            return self.jokes.fetch_joke_norris()
        if joke_type == 'random':
            return self.jokes.fetch_joke_random()

    def get_covid(self):
        return self.covid.fetch_status()
