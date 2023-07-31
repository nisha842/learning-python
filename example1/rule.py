import random

MIN = 1
MAX = 100
NUM_LADDER =  5

def roll():
    return random.randint(1, 6)

def ladder():
    ladder_rule = {}
    for x in range(NUM_LADDER + 1):
        start_point = random.randint(MIN, MAX)
        end_point = random.randint(start_point, MAX)
        ladder_rule[start_point] = end_point
    return ladder_rule

 