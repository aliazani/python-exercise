normal_list = [1, 2, 3, 4, 5]


class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, item):
        return '{x{0}'.format(item)


class FunkyBackwards:
    def __reversed__(self):
        return 'Backwards'


for seq in normal_list, CustomSequence(), FunkyBackwards():
    print(f'\n{seq.__class__.__name__}', end=' ')

for i in reversed(seq):
    print(i, end=', ')
