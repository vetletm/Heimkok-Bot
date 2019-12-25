from typing import Any, List

import json
import random
import os

import praw


class Eyebleacher:
    """
    Retrieves a random top posts from a set of subreddits for cute animals (r/eyebleach, r/aww, etc)
    Will be an improvement on Animals
    Uses the Praw package to interact with Reddit
    """

    def __init__(self):
        """
        Defines start and end of url to scrape and gets all subreddits from file
        """
        if 'REDDIT_CLIENT_ID' in os.environ:
            self.client_id = os.environ['REDDIT_CLIENT_ID']
        else:
            raise ValueError('Missing environment variable: REDDIT_CLIENT_ID')

        if 'REDDIT_CLIENT_ID' in os.environ:
            self.client_secret = os.environ['REDDIT_CLIENT_SECRET']
        else:
            raise ValueError('Missing environment variable: REDDIT_CLIENT_SECRET')

        self.reddit = praw.Reddit(client_id=self.client_id,
                                  client_secret=self.client_secret,
                                  user_agent='Created by u/eyebleacherBot5000')

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
        subreddit = self.subreddits['subreddits'][self._random_index(self.subreddits['subreddits'])]

        # Get post from subreddit
        post = self._get_post(subreddit['subreddit'])

        return post

    def fetch_specific(self, wanted_animal: str) -> str:
        """
        :param wanted_animal: The wanted type of animal
        :return: direct link to the image, gif, or video.
        """
        post = self._get_post(subreddit=self.subreddits[wanted_animal])
        return post

    def _get_post(self, subreddit: str) -> str:
        """
        Returns a random top post from a given subreddit
        :param subreddit: Name of the subreddit
        :return: Direct link to a random post
        """
        return self.reddit.subreddit(subreddit).random().url

    @staticmethod
    def _random_index(arr: List[Any]) -> int:
        """
        Takes a list, finds a random index based on the length and returns the index of the random element
        :param arr: List of any type
        :return: Index as an int
        """
        mod = len(arr)
        n = random.randint(1, 1000)
        return n % mod
