import os

import requests


class Weather:
    def __init__(self):
        """
        :raises ValueError: If OpenWeatherMap API token is missing
        """
        self.prefix = 'https://api.openweathermap.org/data/2.5/weather?q='
        self.suffix = '&units=metric'
        if 'WEATHER_API_TOKEN' in os.environ:
            self.appid = '&appid=' + os.environ['WEATHER_API_TOKEN']
        else:
            raise ValueError('OpenWeatherMap API Token must be given as an environment variable')

    def fetch_weather(self, city):
        """
        :raise: Raises exception from resp.raise_for_status()
        """
        weather_url = f'{self.prefix}{city}{self.suffix}{self.appid}'
        resp = requests.get(weather_url)
        resp.raise_for_status()
        # Craft a neat response on the form:
        '''
        City: Oslo
        Temperature: 3.58℃
        Description: shower rain
        Wind: 5.7m/s, direction: N
        '''
        data = resp.json()
        temp = f'Temperature: {data["main"]["temp"]}' + chr(6541)
        loc = f'City: {data["name"]}'
        desc = f'Description: {data["weather"][0]["description"]}'
        wind_dir = f'{self.degrees_to_cardinal(data["wind"]["deg"])}'
        wind = f'Wind: {data["wind"]["speed"]} m/s, direction: {wind_dir}'

        forecast = '\n'.join([loc, temp, desc, wind])

        return forecast

    # Kudos to https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f for this:
    @staticmethod
    def degrees_to_cardinal(d):
        """
        note: this is highly approximate...
        """
        dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        ix = int((d + 11.25) / 22.5)
        return dirs[ix % 16]
