from typing import Dict, List, Any

import json


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
        self.endpoint = 'http://www.reddit.com/r/'
        self.suffix = '/top/.json?count=20?sort=top&t=day'

        with open('commands/data/subreddits.json', 'r') as file:
            self.subreddits = json.loads(file.read())

    def list_subreddits(self) -> str:
        """
        Will return a list of all available subreddits
        :return: Str of a joined list of subreddits as found in "subreddits.json"
        """
        pass

    def fetch_random(self) -> str:
        """
        Finds a random type from backend json
        :return: direct link to the image, gif, or video.
        """
        pass

    def fetch_specific(self, wanted_animal: str) -> str:
        """
        :param wanted_animal: The wanted type of animal
        :return: direct link to the image, gif, or video.
        """
        pass

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
