class People:
    def __init__(self, age, sex, name):
        self.name = name
        self.age = age
        self.sex = sex

    def happy_birthday(self):
        self.age += 1
        print("happy birthday now you are {}".format(self.age))


ali = People(21, "m", "ali")
ali.happy_birthday()
