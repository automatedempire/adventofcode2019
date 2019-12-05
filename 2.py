#!/usr/bin/env python3

import requests
import os

url='https://adventofcode.com/2019/day/2/input'
dayinput='d2.input'
#Must grab this from a logged in session.
cookiefile='session.cookie'

if not(os.path.exists(dayinput) and os.path.isfile(dayinput)):
    print("Input doesn't exist yet. Downloading...")
    with open(cookiefile) as c:
        cookie=c.readline().strip()
        cookies=dict(session=cookie)
    response = requests.get(url, cookies=cookies)
    with open(dayinput,'w') as d_in:
        d_in.write(response.text)

current_pos = 0

with open(dayinput) as d_in:
    program = [int(x) for x in d_in.readline().split(',')]
    #Restore bad state
    program[1] = 12
    program[2] = 2
    print(program)
    while current_pos < len(program):
        #Read a single instruction
        op = program[current_pos]
        operands = program[current_pos+1:current_pos+3]
        out = program[current_pos + 3]

        #print((op,operands,out))

        #Grab the referenced values
        a = program[operands[0]]
        b = program[operands[1]]

        if op == 1:
            val = a + b
        elif op == 2:
            val = a * b
        elif op == 99:
            break

        program[out] = val
        current_pos += 4

print(program[0])
