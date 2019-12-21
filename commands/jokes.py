# Contains the class for getting funny jokes
import requests, json

'''
Fetches either a specific type of joke or a random one, will update with more sources as I go
'''
class Jokes:
    def __init__(self):
        with open('data/jokes.json', 'r') as f:
            self.jokes = json.loads(f.read())

    def fetch_joke_norris(self):
        url = self.jokes['3']['jokes']['1']['url']
        resp = requests.get(url)
        joke = resp.json()['value']
        return joke

    def fetch_joke_programming(self):
        url = self.jokes['2']['jokes']['1']['url']
        resp = requests.get(url)
        joke = resp.json()[0]['setup'] + ' || ' + resp.json()[0]['punchline'] + ' ||'
        return joke

    def fetch_joke_random(self):
        url = self.jokes['2']['jokes']['2']['url']
        resp = requests.get(url)
        joke = resp.json()['setup'] + ' || ' + resp.json()['punchline'] + ' ||'
        return joke
