class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}:{self.description}'


class Weapon(Item):
    def __init__(self, name, description, power):
        self.power = power
        super().__init__(name, description)


class Inventory:
    def __init__(self):
        self.slot = []

    def add(self, item):
        self.slot.append(item)

    def __len__(self):
        return len(self.slot)

    def __contains__(self, item):
        return item in self.slot

    def __iter__(self):
        yield from self.slot
        # for item in self.slot:
        #     yield item


coin = Item('coin', 'Gold coin')
inv = Inventory()
inv.add(coin)
print(coin in inv)
weapon = Weapon('sword', 'sharp', 40)
weapon2 = Weapon('shotgun', 'shooter', 80)
inv.add(weapon)
inv.add(weapon2)
print(inv.__len__())
for i in inv:
    print(i)
