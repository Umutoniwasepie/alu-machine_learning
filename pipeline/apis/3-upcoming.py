#!/usr/bin/env python3
"""Script that displays the upcoming launch"""

import requests
from datetime import datetime

def get_upcoming_launch():
    """Script that displays the upcoming launch"""

    url = 'https://api.spacexdata.com/v4/launches/upcoming'

    try:
        response = requests.get(url)
        response.raise_for_status()
        launches = response.json()

        # Sort by date_unix to get the soonest upcoming launch
        upcoming_launch = sorted(launches, key=lambda x: x['date_unix'])[0]

        rocket_id = upcoming_launch['rocket']
        rocket_url = f'https://api.spacexdata.com/v4/rockets/{rocket_id}'
        rocket_response = requests.get(rocket_url)
        rocket_response.raise_for_status()
        rocket_name = rocket_response.json()['name']

        launchpad_id = upcoming_launch['launchpad']
        launchpad_url = f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}'
        launchpad_response = requests.get(launchpad_url)
        launchpad_response.raise_for_status()
        launchpad = launchpad_response.json()
        launchpad_name = launchpad['name']
        launchpad_locality = launchpad['locality']

        # Convert and format date to match expected output
        date_local = datetime.fromisoformat(upcoming_launch['date_local'])
        formatted_date = date_local.strftime('%Y-%m-%dT%H:%M:%S%z')

        # Print in the required format
        print(
            "{} ({}) {} - {} ({})".format(
                upcoming_launch['name'], formatted_date, rocket_name,
                launchpad_name, launchpad_locality))

    except requests.RequestException as e:
        print(f'An error occurred while making an API request: {e}')
    except Exception as err:
        print(f'A general error occurred: {err}')

if __name__ == '__main__':
    get_upcoming_launch()
