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
        return sorted(result)


keepers = []
throwers = []

my_dice = Dice()
roll = my_dice.roll()

print("Dice Rolled this throw ", roll)

throwers.clear()

for di in roll:
    print("keep this di", di)
    x = input("Enter Y to keep or N to throw again? ")
    if x != ('y' or 'Y'):
        throwers.append(di)
    else:
        keepers.append(di)

print("Dice kept ", keepers)
print("dice to be thrown ", throwers)

roll = my_dice.roll(int(len(throwers)))
print("Dice Rolled this throw ", roll)
throwers.clear()
for di in roll:
    print("keep this di", di)
    x = input("Enter Y to keep or N to throw again? ")
    if x != ('y' or 'Y'):
        throwers.append(di)
    else:
        keepers.append(di)

print("Dice kept ", keepers)
print("dice to be thrown ", throwers)
