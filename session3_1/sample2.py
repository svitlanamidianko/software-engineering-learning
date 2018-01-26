class Fruit():
    def __init__(self, name, weight_kg):
        self.name = name
        self.weight_kg = weight_kg
        self._ripe = False
        self._rotten = False

    def __repr__(self):
        return "{} ({:.3f}kg)".format(self.name, self.weight_kg)

    def ripen(self):
        if ~self._rotten:
            self._ripe = True
            print("{} is ready to eat!".format(self.name))

    def neglect(self):
        self._rotten = True
        print("Now {} is rotten :'-(".format(self.name))

    def ready_to_eat(self):
        return self._ripe and not self._rotten

from enum import Enum

class Cooked(Enum):
    BOILED = 1
    FRIED = 2
    ROAST = 3

class Vegetable():
    def __init__(self, name):
        self.name = "Vegetable " + name
        self.cooked = None
        print("Vegetable Initialized")

    def fry(self):
        self.cooked = Cooked.FRIED


class Tomato(Fruit, Vegetable):
    def __init__(self, name='Tomato', weight_kg=3.0):
        Fruit.__init__(self, name=name, weight_kg=weight_kg)
        Vegetable.__init__(self, name=name)


t = Tomato()
t.fry()
print(t)
