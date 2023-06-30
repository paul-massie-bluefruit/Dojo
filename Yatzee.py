"""
Ultimate objctive
create a Yatzee game 

learning goals
1. create a class for a dice.
2. random number genarator for the dice when rolled
3. Evaluate dice outcome and assign result to player score


"""
import numpy as np
import random

class Dice:
    def __init__(self, sides, current_value):
        self.sides = 6
        self.current_value = 0

    def roll(self):
        self.current_value = random.randint(1, 6)
        print(self.current_value)

di = Dice(6,0)
di.roll(1)
    


