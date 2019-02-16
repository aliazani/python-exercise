class Thief:
    sneaky = True

    def pick_pocket(self, light_level):
        return self.sneaky and light_level == 10


ali = Thief()
reza = Thief()
ali.pick_pocket(10)
Thief.pick_pocket(reza, 9)
