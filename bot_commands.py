from commands.weather import Weather
from commands.animals import Animals


class BotCommands:
    """
    Wrapper class for all functionality
    """
    def __init__(self):
        self.weather = Weather()
        self.animals = Animals()

    def get_weather(self, city):
        return self.weather.fetch_weather(city)

    def get_animal(self, kind):
        return self.animals.fetch_animalpic(kind)
