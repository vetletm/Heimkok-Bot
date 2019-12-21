from weather import Weather


class BotCommands:
    """
    Wrapper class for all functionality
    """
    def __init__(self):
        self.weather = Weather()

    def get_weather(self, city):
        return self.weather.fetch_weather(city)
