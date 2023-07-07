"""
LEARNING OBJECTIVE

    -   find a way to have all the classes within this file
            and import them where needed?
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


class Player:
    def __init__(self, name="Player 1"):
        self.name = name
        self.roll = sorted([])
        self.keepers = sorted([])
        self.throwers = sorted([])
