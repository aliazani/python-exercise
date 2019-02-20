class Reverse(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


pat = Reverse('abcdefg')
print(pat)
