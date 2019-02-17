import random


class Character:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    sneaky = True

    def __init__(self, **kwargs):
        self.sneaky = True
        super().__init__(**kwargs)

    def pick_pocket(self):
        return bool(random.randint(0, 1)) and self.sneaky

    def hide(self, light_level):
        return self.sneaky and light_level == 10


ali = Thief(weapn="knife", car="Peugeot 206")
ali.hide(10)
print(ali.car)
print(ali.sneaky)
