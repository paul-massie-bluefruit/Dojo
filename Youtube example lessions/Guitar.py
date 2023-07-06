class Guitar:
    def __init__(self, n_strings=6):
        self.n_strings = n_strings
        self.play()
        self.__cost = 50

    def play(self):
        print("pam pam pam pam pam pam ")


class BassGuitar(Guitar):
    pass


class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__(n_strings=8)
        self.colour = ("000000", "FFFFFF")

    def playLoader(self):
        print("pam pam pam pam pam pam ".upper())

    def __secret(self):
        print("this guitar cost me £", self._Guitar__cost, "only!")


my_guitar = ElectricGuitar()
my_guitar._ElectricGuitar__secret()
my_guitar.playLoader()
print("my base has ", BassGuitar(4).n_strings, "Strings")
print("my electric has ", ElectricGuitar().n_strings, "Strings")
