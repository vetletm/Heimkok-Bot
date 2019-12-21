from commands.weather import Weather
from commands.animals import Animals
from commands.jokes import Jokes


class BotCommands:
    """
    Wrapper class for all functionality
    """
    def __init__(self):
        self.weather = Weather()
        self.animals = Animals()
        self.jokes = Jokes()

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
