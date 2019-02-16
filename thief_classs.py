import random


class Thief:
    sneaky = True

    def pick_pocket(self):
        if self.sneaky:
            return bool(random.randint(0, 1))
        return False

    def hide(self, light_level):
        return self.sneaky and light_level == 10


ali = Thief()
ali.hide(10)
