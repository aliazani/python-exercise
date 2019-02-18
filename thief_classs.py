import random


class Sneaky:
    sneaky = True

    def __init__(self, sneaky=True, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.sneaky = sneaky

    def hide(self, light_level):
        return self.sneaky and light_level > 10


class Agile:
    agile = True

    def __init__(self, agile=True, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.agile = agile

    def evade(self):
        return self.agile and bool(random.randint(0, 1))


class Character:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character, Agile, Sneaky):
    sneaky = True

    def __init__(self, name, **kwargs):

        self.name = name
        super().__init__(**kwargs)


ali = Thief("ali", weapn="knife", car="Peugeot 206")
ali.hide(10)
print(ali.car)
print(ali.sneaky)
print(ali.hide(4))
print(ali.agile)
print(issubclass(Thief, Character))
print(type(ali))
print(ali.__class__.__name__)


