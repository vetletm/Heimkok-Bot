from typing import Dict, Any, Tuple

import json
import random
import requests


class Eyebleacher:
    """
    Retrieves a random top posts from a set of subreddits for cute animals (r/eyebleach, r/aww, etc)
    Will be an improvement on Animals
    TODO:
        - Implement persistent storage in the form of JSON, just as Animals-class.
            - Search all files starting with subreddit for name as a suffix
        - Can either use praw for direct interaction with Reddit API, or:
        - Use requests to manually scrape the json data from a subreddit
        - upgrade to pycharm when possible....

    If using requests the flow will be:
        - fetch subreddit from self.subreddits
        - fetch json-content of subreddit
            - maybe limit to once a day by storing current top posts with date and
                if date is not today, refresh content
        - pick top post from subreddit content
        - return top post

    Using requests might result in response 429 from Reddit, if this turns out to be
    a persistent issue, reconsider using Praw.
    """

    def __init__(self):
        """
        Defines start and end of url to scrape and gets all subreddits from file
        """
        self.endpoint = 'http://www.reddit.com/r/'
        self.suffix = '/top/.json?count=20?sort=top&t=day'

        with open('commands/data/subreddits.json', 'r') as file:
            self.subreddits = json.loads(file.read())

    def list_subreddits(self) -> str:
        """
        Will return a list of all available subreddits
        :return: Str of a joined list of subreddits as found in "subreddits.json"
        """
        s_list = ', '.join([subreddit['subreddit'] for subreddit in self.subreddits['subreddits']])
        return s_list

    def fetch_random(self) -> str:
        """
        Finds a random type from backend json
        :return: direct link to the image, gif, or video.
        """
        # Find a random index from list of subreddits
        mod = len(self.subreddits['subreddits'])
        n = random.randint(1, 1000)
        subreddit = self.subreddits['subreddits'][n % mod]

        # Get post from subreddit
        post = self._get_post(subreddit['subreddit'])

        return post

    def fetch_specific(self, wanted_animal: str) -> str:
        """
        :param wanted_animal: The wanted type of animal
        :return: direct link to the image, gif, or video.
        """
        pass

    def _get_post(self, subreddit: str) -> str:
        """
        Returns a random top post from a given subreddit
        :param subreddit: Name of the subreddit
        :return: Direct link to a random post
        """
        # calls _get_state for content
        subreddit_state = self._get_state(subreddit)

        # get random post
        mod = len(subreddit_state['data']['children'])
        n = random.randint(1, 1000)
        post = subreddit_state['data']['children'][n % mod]['data']['url']

        return post

    def _get_state(self, subreddit: str) -> Dict[str, Tuple[Any]]:
        """
        Gets the current state of given subreddit
        TODO:
            - Update to use _store_state and _update_state if state of subreddit is a day old
            - Update to use regex to find the file with the subreddit content
        :param subreddit: Name of subreddit
        :return: Content of the subreddit
        """
        # Simply get state from reddit for now
        url = f'{self.endpoint}{subreddit}{self.suffix}'
        content = requests.get(url)

        content.raise_for_status()

        content = json.loads(content)

        return content

    def _store_state(self, subreddit: Dict[str, Tuple[Any]]) -> bool:
        """
        Will store the state of the subreddit in a json-file
        :param subreddit: Dictionary of the subreddit data
        :return: Boolean, True if successful, False if it failed
        """
        pass

    def _update_state(self, subreddit: str) -> bool:
        """
        Stores the state of the subreddit data to avoid too many calls to reddit,
        if the state is not stored create new file with name "subreddit_name.json"
        """
        pass
