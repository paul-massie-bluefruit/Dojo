class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("hello my name is " + self.name, self.age)


p1 = Person("Scotty", 39)

p1.myfunc()
