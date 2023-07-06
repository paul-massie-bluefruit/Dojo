"""
PSEDO CODE
throw_dice() # initial trow 
decide() # decide which dice to keep - end turn ?
throw_dice() #2nd throw
decide() # decide which dice to keep - end turn ?
throw_dice() # final throw, end of turn

"""
import random
from Classes_Yatzee import *

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self, di_rolled=5):
        self.di_rolled = di_rolled
        result = []
        while di_rolled > 0:
            result.append(random.randint(1, self.sides))
            di_rolled -= 1
        return sorted(result)


class Player:
    def __init__(self, name="Player 1"):
        self.name = name
        self.roll = sorted([])
        self.keepers = sorted([])
        self.throwers = sorted([])

#class initallised
my_dice = Dice()
p1 = Player()
    

def decide():
    print("Thrown dice result: ", p1.roll)
    p1.throwers.clear()
    for di in p1.roll:
        print( "keep this di:", di)
        x = input("Enter Y to keep or N to throw again? ")
        if x != ('y' or 'Y'):
            p1.throwers.append(di)
        else:
            p1.keepers.append(di)


def turn_throw(n):
    if n == 0:
        n += 5
    else:
        n = len(p1.throwers)
    p1.roll = sorted(my_dice.roll(n))

def total_dice_value(lst):
    score = 0
    for i in lst:
        score += i
    print(score)
    
    
roll_total = 0
while roll_total < 3 and len(p1.keepers)  !=5:   
    turn_throw(int(len(p1.throwers)))
    decide()
    roll_total +=1
    print("Dice to keep: ", p1.keepers)

print("Score", p1.keepers + p1.throwers)
total_dice_value(p1.keepers + p1.throwers)



"""
 where are we - a player can roll the dice and decide which to keep, and re-roll upto 3 times.

 What's next?   - create class for score card
                - abiity to add dice total to score card
                - create logic for scoring rules - see Yatzee_rules.pdf
PSEDO CODE

Score()# calculate score
scorecard.
"""
