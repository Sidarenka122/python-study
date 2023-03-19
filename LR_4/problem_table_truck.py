class Table:
    def __init__(self, weight):
        self.weight = weight


class Truck:
    SUCCESS = "cargo was added successfully"
    DOESNT_FIT = 'cargo doesn"t fit the truck free space'
    FULL = 'truck is full'

    def __init__(self, capacity):
        self.__capacity = capacity
        self.freeSpace = capacity

    def unload_truck(self):
        self.freeSpace = self.__capacity

    def add_cargo(self, weight):
        new_free_space = self.freeSpace - weight
        if new_free_space > 0:
            self.freeSpace = new_free_space
            print(Truck.SUCCESS)
            return Truck.SUCCESS
        elif new_free_space < 0:
            print(Truck.DOESNT_FIT)
            return Truck.DOESNT_FIT
        else:
            print(Truck.FULL)
            return Truck.FULL


tableWeight = int(input("Enter table weight \n"))
truckCapacity = int(input("Enter truck capacity \n"))

table = Table(tableWeight)
truck = Truck(truckCapacity)

while truck.add_cargo(table.weight) != Truck.FULL:
    tableWeight = int(input("Enter table weight \n"))
    table = Table(tableWeight)
