import json
import random

import requests


class Animals:
    """
    Gets its picture sources from a .json file, want to update to use Postgres instead
    """

    # Animal dictionary to fetch a random animal picture
    def __init__(self):
        # Reads jsonfile with all animals
        with open('commands/data/animals.json', 'r') as f:
            self.animals = json.loads(f.read())

    def fetch_animalpic(self, kind):
        # Either random or specific, based on !cuteanimal or !cuteanimal <animal>
        animal = None
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

        if not animal:
            return 'Could not fetch cute pic'
        # Attempt to fetch the direct link to the animal picture
        resp = requests.get(animal['url'])

        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return 'Could not fetch cute pic, sorry. Reason: ' + str(e)
        return resp.json()[animal['file']]

    # Returns a neat cat fact
    @staticmethod
    def fetch_catfact():
        resp = requests.get('https://cat-fact.herokuapp.com/facts/random')
        return resp.json()['text']
