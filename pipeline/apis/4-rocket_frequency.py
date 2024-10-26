#!/usr/bin/env python3
"""Script that displays the number of launches per rocket"""

import requests
from collections import defaultdict

def get_launches_per_rocket():
    launches_url = 'https://api.spacexdata.com/v4/launches'
    rockets_url = 'https://api.spacexdata.com/v4/rockets'

    try:
        launches = requests.get(launches_url).json()
        launch_count = defaultdict(int)

        for launch in launches:
            rocket_id = launch['rocket']
            launch_count[rocket_id] += 1

        rockets = requests.get(rockets_url).json()
        rocket_names = {rocket['id']: rocket['name'] for rocket in rockets}

        rocket_launches = [
            (rocket_names[rocket_id], count)
            for rocket_id, count in launch_count.items()
        ]

        rocket_launches.sort(key=lambda x: (-x[1], x[0]))

        for rocket, count in rocket_launches:
            print(f"{rocket}: {count}")

    except requests.RequestException as e:
        print(f'An error occurred while making an API request: {e}')
    except Exception as err:
        print(f'A general error occurred: {err}')

if __name__ == '__main__':
    get_launches_per_rocket()
