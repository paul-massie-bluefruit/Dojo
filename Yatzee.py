"""
Ultimate objctive
create a Yatzee game

learning goals
1. create a class for a dice.
2. random number genarator for the dice when rolled
3. Evaluate dice outcome and assign result to player score


"""
import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self, di_rolled=5):
        self.di_rolled = di_rolled
        result = []
        while di_rolled > 0:
            result.append(random.randint(1, self.sides))
            di_rolled -= 1
            
        return result

keep_di = []
throw_di = []
my_dice = Dice()
roll = my_dice.roll()
print(roll)
for di in roll:
    print("keep this di", di)
    x = input("Enter Y to keep or N to throw again? ")
    if x != ('y' or 'Y'):
        throw_di.append(di)
    else:
        keep_di.append(di)

print(keep_di)
print(throw_di)
