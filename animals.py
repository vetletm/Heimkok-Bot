# Contains the class for getting pictures of animals
import requests, json, random
'''
Gets its picture sources from a .json file, want to update to use Postgres instead
'''
class Animals:
    # Animal dictionary to fetch a random animal picture
    def __init__(self):
        # Reads jsonfile with all animals
        with open('animals.json', 'r') as f:
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
