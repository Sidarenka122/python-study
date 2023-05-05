from LR_4.problem_3 import House

class MagicHouse(House):
    def __init__(self, color, *args):
        super(MagicHouse, self).__init__(*args)
        self.color = color
    def __str__(self):
        return '{0} - {1}'.format(self.__class__.__name__, self.__dict__)

    def __del__(self):
        MagicHouse._id -= 1
        print(MagicHouse._id)

    def __eq__(self, other):
        return self.get_build_year() == other.get_build_year()

    def __add__(self, other):
        return self.get_lifetime() + other.get_lifetime()

    def __getattr__(self, item):
        print("Attr " + str(item) + " is not implemented")
        raise AttributeError

# __new__ and __init__ from House file
extendedHouse3 = MagicHouse('white', 1500, 77, 40, 1, 1, 'Pushkina', 'panel', 50)
extendedHouse4 = MagicHouse('ochre', 1500, 20, 11, 2, 3, 'Shupkina', 'panel', 34)

print(extendedHouse3) # __str__
print(extendedHouse3 == extendedHouse4) # __eq__
print(extendedHouse3 + extendedHouse3) # __add__
print(extendedHouse3.hello) # __getattr__

# __del__