import json


class Eyebleacher:
    """
    Retrieves a random top posts from a set of subreddits for cute animals (r/eyebleach, r/aww, etc)
    Will be an improvement on Animals
    TODO:
        - Implement persistent storage in the form of JSON, just as Animals-class.
        - Can either use praw for direct interaction with Reddit API, or:
        - Use requests to manually scrape the json data from a subreddit

    If using requests the flow will be:
        - fetch subreddit from self.subreddits
        - fetch json-content of subreddit
            - maybe limit to once a day by storing current top posts with date and
                if date is not today, refresh content
        - pick top post from subreddit content
        - return top post
    """
    def __init__(self):
        self.endpoint = 'api/v1/something'
        self.creds = {'user': 'someUser', 'id': 'someId'}

        with open('commands/data/subreddits.json', 'r') as file:
            self.subreddits = json.loads(file.read())

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
