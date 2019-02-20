class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}:{self.description}'


class Weapon(Item):
    def __init__(self, name, descripton, power):
        super.__init__(name, descripton)
        self.power = power
