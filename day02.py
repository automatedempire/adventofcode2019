#!/usr/bin/env python3

import requests
import os

url='https://adventofcode.com/2019/day/2/input'
dayinput='input/d2.input'
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

with open(dayinput) as d_in:
    initial_program = [int(x) for x in d_in.readline().split(',')]

def run_program(noun, verb):
    current_pos = 0
    program = initial_program.copy()

    #Induce bad state
    program[1] = noun
    program[2] = verb

    while current_pos < len(program):
        #Read a single instruction
        op = program[current_pos]
        operands = program[current_pos+1:current_pos+3]
        out = program[current_pos + 3]

        #print((op,operands,out))

        #Grab the referenced values
        a = program[operands[0]]
        b = program[operands[1]]

        val = 0
        if op == 1:
            val = a + b
        elif op == 2:
            val = a * b
        elif op == 99:
            break

        if out < len(program):
            program[out] = val
        current_pos += 4

    return program[0]

#Print output for part 1
print(f"Part 1: {run_program(12,2)}")

#Part 2: Search for a desired output.
for (noun,verb) in [(x,y) for x in range(99) for y in range(99)]:
    output = run_program(noun, verb)

    desired_output = 19690720

    if output == desired_output:
        print(f"The magic numbers are {noun} and {verb}: {100 * noun + verb}")
        break
