from random import randint


class Thief:
    sneaky = True

    def pick_pocket(self):
        return bool(randint(0, 1))
