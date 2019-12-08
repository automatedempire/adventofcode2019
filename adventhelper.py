#!/usr/bin/env python3

import requests
import os

def download_input(day):
    dayinput=f'input/d{day}.input'

    if not(os.path.exists(dayinput) and os.path.isfile(dayinput)):
        print("Input doesn't exist yet. Downloading...")
        url=f'https://adventofcode.com/2019/day/{day}/input'
        #Must grab this from a logged in session.
        cookiefile='session.cookie'
        with open(cookiefile) as c:
            cookie=c.readline().strip()
            cookies=dict(session=cookie)
        response = requests.get(url, cookies=cookies)
        with open(dayinput,'w') as d_in:
            d_in.write(response.text)

    return dayinput
