# Contains the class for getting the weather
import requests, os
'''
This class uses the OpenWeatherMap API, free edition.
'''
class Weather:
    def __init__(self):
        self.prefix = 'https://api.openweathermap.org/data/2.5/weather?q='
        self.suffix = '&units=metric'
        if 'WEATHER_API_TOKEN' in os.environ:
            self.appid = '&appid=' + os.environ['WEATHER_API_TOKEN']
        else:
            print('WEATHER_API_TOKEN must be passed as an environment variable')
            exit(1)

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
