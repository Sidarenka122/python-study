class Table:
    def __init__(self, weight):
        self.weight = weight


class Truck:
    SUCCESS = "cargo was added successfully"
    DOESNT_FIT = 'cargo doesn"t fit the truck free space'
    FULL = 'truck is full'

    def __init__(self, capacity):
        self.__capacity = capacity
        self.free_space = capacity

    def unload_truck(self):
        self.free_space = self.__capacity

    def add_cargo(self, weight):
        new_free_space = self.free_space - weight
        if new_free_space > 0:
            self.free_space = new_free_space
            print(Truck.SUCCESS)
            return Truck.SUCCESS
        elif new_free_space < 0:
            print(Truck.DOESNT_FIT)
            return Truck.DOESNT_FIT
        else:
            self.free_space = 0
            print(Truck.FULL)
            return Truck.FULL


def add_cargo_example():
    table_weight = int(input("Enter table weight \n"))
    truck_capacity = int(input("Enter truck capacity \n"))

    table = Table(table_weight)
    truck = Truck(truck_capacity)

    while truck.add_cargo(table.weight) != Truck.FULL:
        table_weight = int(input("Enter table weight \n"))
        table = Table(table_weight)
