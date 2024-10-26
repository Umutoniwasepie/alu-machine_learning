#!/usr/bin/env python3
"""Script that displays the upcoming launch"""

import requests
from datetime import datetime

def get_upcoming_launch():
    url = 'https://api.spacexdata.com/v4/launches/upcoming'
    try:
        response = requests.get(url)
        response.raise_for_status()
        launches = response.json()
        upcoming_launch = sorted(launches, key=lambda x: x['date_unix'])[0]

        rocket_id = upcoming_launch['rocket']
        rocket_url = f'https://api.spacexdata.com/v4/rockets/{rocket_id}'
        rocket = requests.get(rocket_url).json()

        launchpad_id = upcoming_launch['launchpad']
        launchpad_url = f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}'
        launchpad = requests.get(launchpad_url).json()

        launch_date = datetime.fromisoformat(upcoming_launch['date_local']).strftime('%Y-%m-%d %H:%M:%S')

        print(f"{upcoming_launch['name']} ({launch_date}) {rocket['name']} - {launchpad['name']} ({launchpad['locality']})")

    except requests.RequestException as e:
        print(f'An error occurred while making an API request: {e}')
    except Exception as err:
        print(f'A general error occurred: {err}')

if __name__ == '__main__':
    get_upcoming_launch()
