import random


class Thief:
    sneaky = True

    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def pick_pocket(self):
            return bool(random.randint(0, 1)) and self.sneaky

    def hide(self, light_level):
        return self.sneaky and light_level == 10


ali = Thief("ali", weapn="knife", car="206")
ali.hide(10)