from datetime import datetime, timedelta

import requests


class Covid:
    """
    Fetches the current status of COVID-19 cases in Norway
    """

    def __init__(self):
        """
        No Token required, but rate is limited
        """
        self.url = 'https://api.covid19api.com/country/norway'

    def fetch_status(self):
        """
        Takes current datetime and formats to be YYYY-mm-ddTHH:MM:SSZ
        """
        # Time from 7 days ago until yesterday
        current_date = datetime.now() - timedelta(days=1)
        one_week = datetime.now() - timedelta(days=7)

        now = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        then = one_week.strftime("%Y-%m-%dT%H:%M:%SZ")

        resp = requests.get(f'{self.url}?from={then}&to={now}')
        covid = resp.json()

        confirmed = covid[-1]['Confirmed']
        active = covid[-1]['Active']
        change = covid[-1]['Active'] - covid[0]['Active']

        status = f'Confirmed per {current_date.strftime("%A, %B %d")}: {confirmed}, current active cases: {active},' \
                 f' which is an increase of {change} from {one_week.strftime("%A, %B %d")}.'

        return status
