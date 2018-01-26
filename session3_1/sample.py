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


class Banana(Fruit):
    def __init__(self, name='Banana', weight_kg=0.2):
        super().__init__(name, weight_kg)
        self._peeled = False

    def peel(self):
        self._peeled = True

    def ready_to_eat(self):
        if self._peeled:
            return super().ready_to_eat()
        return False
#-----

class Chef():
    def __init__(self):
        self.fruit = []

    def ripen(self):
        for f in self.fruit:
            f.ripen()

    def neglect(self):
        for f in self.fruit:
            f.neglect()

    def get_ready_to_eat(self):
        return [f for f in self.fruit if f.ready_to_eat()]

    def get_not_ready_to_eat(self):
        return [f for f in self.fruit if not f.ready_to_eat()]

    def get_fruit_salad(self):
        ans = []
        for f in self.get_ready_to_eat():
            (num_slices, remainder) = divmod(f.weight_kg, 0.05)
            print(f.name, num_slices, remainder)
            for a in range(int(num_slices)):
                ans.append(Fruit(f.name + ' Slice', 0.05))
            if remainder > 1e-16:
                ans.append(Fruit(f.name + ' Slice', remainder))
        self.fruit = self.get_not_ready_to_eat()
        return ans

from enum import Enum

#-----

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
    def __init__(self, name='Tomato', weight_kg=1.0):
        Fruit.__init__(self, name=name, weight_kg=weight_kg)
        Vegetable.__init__(self, name=name)


s = Fruit('Strawberry', 0.05)
a = Fruit('Apple', 0.25)
b = Banana()
s.ripen()
a.neglect()
b.ripen()
b.peel()

t = Tomato()
t.fry()
t.ripen()
print(t)


chef = Chef()
chef.fruit = [s, a, b, t]
if isinstance(chef, Fruit):
    print("Chef is type of a Fruit??")
else:
    print("Chef is not a type of Fruit")

print(chef.get_fruit_salad())
