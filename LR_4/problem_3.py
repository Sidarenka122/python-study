# Задача 3
# Kласс House: id, Номер квартиры, Площадь, Этаж,
# Количество комнат, Улица, Тип здания, Срок эксплуатации.

# Функции-члены реализуют
# запись и считывание полей (проверка корректности),
# расчета возраста задания (необходимость в кап. ремонте).

# Создать список объектов. Вывести:
# список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и
# расположенных на этаже, который находится в заданном промежутке;

import datetime


class ArrayHelper:
    @staticmethod
    def print(array):
        if len(array) == 0:
            print('no items found')
        else:
            for i in range(len(array)):
                print(array[i])


class Validity:
    @staticmethod
    def is_valid_integer(val):
        try:
            int_value = int(val)
            is_valid = int_value >= 0
            if not is_valid:
                print('Number is invalid')
            return is_valid
        except:
            print('Number is invalid')
            return False

    @staticmethod
    def is_valid_string(val):
        try:
            str_value = str(val)
            is_valid = len(str_value) > 0
            if not is_valid:
                print('String is invalid')
            return is_valid
        except:
            print('String is invalid')
            return False

    @staticmethod
    def is_valid_float(val):
        try:
            float_value = float(val)
            is_valid = float_value >= 0
            if not is_valid:
                print('Float is invalid')
            return is_valid
        except:
            print('Float is invalid')
            return False


class House:
    __id = 0

    @staticmethod
    def find_buildings_with_number_of_rooms(buildings_array, room_number):
        def check_room_number(building):
            return building.__room_number == room_number

        return list(filter(check_room_number, buildings_array))

    @staticmethod
    def find_buildings_on_the_floor_with_room_number(buildings_array, room_number, min_floor, max_floor):
        if min_floor > max_floor or max_floor == 0:
            print('invalid min max floor')
            return []
        buildings_with_room_number = House.find_buildings_with_number_of_rooms(buildings_array, room_number)

        if len(buildings_with_room_number) == 0:
            return []

        def check_floor_range(building):
            return min_floor <= building.__floor <= max_floor

        buildings_in_the_floor_range = list(filter(check_floor_range, buildings_with_room_number))

        return buildings_in_the_floor_range

    def __init__(self, build_year, apartment_number, square_ft, floor, room_number, street, building_type,
                 lifetime):
        self.__apartment_number = apartment_number
        self.__square_ft = square_ft
        self.__floor = floor
        self.__room_number = room_number
        self.__street = street
        self.__building_type = building_type
        self.__lifetime = lifetime
        self.__build_year = build_year
        self.__id += 1

    def get_building_id(self):
        return self.__id

    def get_apartment_number(self):
        return self.__apartment_number

    def set_apartment_number(self, apartment_number):
        if Validity.is_valid_integer(apartment_number):
            self.__apartment_number = apartment_number

    def get_square_ft(self):
        return self.__square_ft

    def set_square_ft(self, square_ft):
        if Validity.is_valid_float(square_ft):
            self.__square_ft = square_ft

    def get_floor(self):
        return self.__floor

    def set_floor(self, floor):
        if Validity.is_valid_integer(floor):
            self.__floor = floor

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        if Validity.is_valid_integer(room_number):
            self.__room_number = room_number

    def get_street(self):
        return self.__street

    def set_street(self, street):
        if Validity.is_valid_string(street):
            self.__street = street

    def get_building_type(self):
        return self.__building_type

    def set_building_type(self, building_type):
        if Validity.is_valid_string(building_type):
            self.__building_type = building_type

    def get_lifetime(self):
        return self.__lifetime

    def set_lifetime(self, lifetime):
        if Validity.is_valid_integer(lifetime):
            self.__lifetime = lifetime

    def get_build_year(self):
        return self.__lifetime

    def set_build_year(self, build_year):
        if Validity.is_valid_integer(build_year):
            self.__build_year = build_year

    def needs_fix(self):
        return self.__lifetime - self.building_age() < 0

    def building_age(self):
        current_year = datetime.date.today().year

        return current_year - self.__build_year

    def __str__(self):
        return self.__street + " " + str(self.__apartment_number) + "\n"


# б) список квартир, имеющих заданное число комнат и
# расположенных на этаже, который находится в заданном промежутке;

building1 = House(2020, 82, 78, 2, 3, 'Novovilenskaya', 'block', 40)
building2 = House(1999, 77, 40, 1, 1, 'Pushkina', 'panel', 50)
building3 = House(2001, 34, 40, 2, 1, 'Kolasa', 'panel', 45)
building4 = House(2000, 12, 85, 8, 3, 'Odoevskogo', 'panel', 50)
building5 = House(2011, 109, 45, 8, 1, 'Beruta', 'wood', 25)
building6 = House(1999, 5, 55, 4, 2, 'Mavra', 'block', 40)

# buildings = [building1, building2, building3, building4, building5, building6]
buildings = [building2]

room_number = input("Enter room number \n")

if Validity.is_valid_integer(room_number):
    ArrayHelper.print(House.find_buildings_with_number_of_rooms(buildings, int(room_number)))

print('************************')

floor_min = input("Enter min floor \n")
floor_max = input("Enter max floor \n")

print('************************')

if Validity.is_valid_integer(floor_min) & Validity.is_valid_integer(floor_max):
    ArrayHelper.print(House.find_buildings_on_the_floor_with_room_number(buildings, int(room_number), int(floor_min),
                                                                         int(floor_max)))
