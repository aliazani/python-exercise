class Protected:
    __name = 'security'

    def __method(self):
        return self.__name


instance = Protected
print(dir(instance))
print(instance._Protected__method)

print(instance._Protected__name)
