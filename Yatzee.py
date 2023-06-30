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
    def __init__(self,):
      self.sides = 6

    def roll(self):
       return random.randint(1, self.sides)

my_dice = Dice()
result = my_dice.roll()
print(result)
  
    


