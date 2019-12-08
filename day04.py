#!/usr/bin/env python3

from adventhelper import download_input
import re

#Input is provided directly on the site rather than a file. I created a file anyway.
#Adventhelper will return the proper name, but will not download this file.
dayinput = download_input(day=4)

with open(dayinput) as d_in:
    minpass, maxpass = [int(x) for x in d_in.readline().split('-')]

#two of the same digit together
doubles = re.compile(r"(.)\1")
justdoubles = re.compile(r"(.)\1(?<!\1{3})(?!\1)")

possibilities = []
betterpossibilities = []

for x in range(minpass,maxpass):
    numstring = str(x)
    hasdouble = doubles.search(numstring)
    justdouble = justdoubles.search(numstring)
    s = "".join(sorted(numstring))
    inOrder = numstring == s

    if hasdouble and inOrder:
        possibilities.append(x)

    if justdouble and inOrder:
        betterpossibilities.append(x)

print(f"Total possible passwords: {len(possibilities)}")
print(f"Total better possible passwords: {len(betterpossibilities)}")
