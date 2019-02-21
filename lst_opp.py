from copy import copy


class FilledList(list):
    def __init__(self, value, count, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy(value))


l1 = FilledList(1, 10)
print(l1)
print(len(l1))
