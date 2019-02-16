# training
from random import randint


class Thief:
    sneaky = True

    def pick_pocket(self):
        if self.sneaky:
            print("called by {}".format(self))
            return bool(randint(0, 1))
        return False


ali = Thief()
reza = Thief()
ali.pick_pocket()
Thief.pick_pocket(reza)
