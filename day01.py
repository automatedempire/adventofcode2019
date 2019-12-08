#!/usr/bin/env python3

import requests
import os
from math import floor

url='https://adventofcode.com/2019/day/1/input'
d1input='input/d1.input'
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
fuel_fuel = 0

def fuelinception(fuel):
    if fuel <= 0:
        return 0
    extrafuel = max(floor(fuel / 3) - 2, 0)
    return extrafuel + fuelinception(extrafuel)

with open(d1input) as d1i:
    for i in d1i:
        mod_weight=int(i)
        #print(mod_weight)
        fuel=floor(mod_weight / 3) - 2
        totalfuel += fuel
        fuel_fuel += fuelinception(fuel)

print(f"Initial fuel requirement: {totalfuel}")
print(f"Fuel fuel: {fuel_fuel}")

print(f"Total fuel requirement: {totalfuel + fuel_fuel}")
