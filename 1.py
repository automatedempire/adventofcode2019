#!/usr/bin/env python3

import requests
import os
from math import floor

url='https://adventofcode.com/2019/day/1/input'
d1input='d1input'
#Must grab this from a logged in session.
cookiefile='session.cookie'

if not(os.path.exists(d1input) and os.path.isfile(d1input)):
    print("Input doesn't exist yet. Downloading...")
    with open(cookiefile) as c:
        cookie=c.readline().strip()
        cookies=dict(session=cookie)
    response = requests.get(url, cookies=cookies)
    with open(d1input,'w') as d1i:
        d1i.write(response.text)

totalfuel = 0

with open(d1input) as d1i:
    for i in d1i:
        mod_weight=int(i)
        #print(mod_weight)
        fuel=floor(mod_weight / 3) - 2
        totalfuel += fuel

print(f"Initial fuel requirement: {totalfuel}")
