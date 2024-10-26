#!/usr/bin/env python3

<<<<<<< HEAD
"""Script that prints the location of a specific user"""
=======

""" Return location of a GitHub user or provide rate limit informatin"""
>>>>>>> d9d3bba5594651a2f71b17289ac7454970d7a977

import requests
import sys
import time


if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if res.status_code == 403:
        rate_limit = int(res.headers.get('X-Ratelimit-Reset'))
        current_time = int(time.time())
<<<<<<< HEAD
        diff = int((rate_limit - current_time) / 60)
        print('Reset in {} min'.format(int(diff)))
=======
        diff = (rate_limit - current_time) // 60
        print("Reset in {} min".format(diff))
        # get remaining rate
>>>>>>> d9d3bba5594651a2f71b17289ac7454970d7a977

    elif res.status_code == 404:
        print("Not found")
    elif res.status_code == 200:
        res = res.json()
        print(res['location'])
