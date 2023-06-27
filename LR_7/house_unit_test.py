from LR_4.problem_3 import House
import unittest


class HouseTest(unittest.TestCase):
    house = None
    buildings = []

    @classmethod
    def setUpClass(cls):
        print("Starting tests for House Class..")
        building1 = House(2020, 82, 78, 2, 3, 'Novovilenskaya', 'block', 40)
        building2 = House(1999, 77, 40, 1, 1, 'Pushkina', 'panel', 50)
        building3 = House(2001, 34, 40, 2, 1, 'Kolasa', 'panel', 45)
        building4 = House(2000, 12, 85, 8, 3, 'Odoevskogo', 'panel', 50)
        building5 = House(2011, 109, 45, 8, 1, 'Beruta', 'wood', 25)
        building6 = House(1999, 5, 55, 4, 2, 'Mavra', 'block', 40)
        cls.buildings = [building1, building2, building3, building4, building5, building6]

    @classmethod
    def tearDownClass(cls):
        print("End tests for House Class!")

    def setUp(self):
        """Set Up Method!"""
        print("Initialize house for [" + self.shortDescription() + "]")
        self.house = House(2020, 82, 78, 2, 3, 'Novovilenskaya', 'block', 40)

    def test__init__(self):
        """Init Method!"""
        self.assertEqual(self.house.get_apartment_number(), 82)
        self.assertEqual(self.house.get_square_ft(), 78)
        self.assertEqual(self.house.get_floor(), 2)
        self.assertEqual(self.house.get_room_number(), 3)
        self.assertEqual(self.house.get_street(), 'Novovilenskaya')
        self.assertEqual(self.house.get_building_type(), 'block')
        self.assertEqual(self.house.get_lifetime(), 40)

    def test_set_apartment_number(self):
        """set_apartment_number Method!"""
        self.assertEqual(self.house.get_apartment_number(), 82)

        self.house.set_apartment_number(33)
        self.assertEqual(self.house.get_apartment_number(), 33)

    def test_not_set_negative_numbers_for_apartment(self):
        """set_apartment_number no negative numbers!"""
        self.assertEqual(self.house.get_apartment_number(), 82)

        self.house.set_apartment_number(-1)
        self.assertEqual(self.house.get_apartment_number(), 82)

    def test_not_set_characters_as_apartment_number(self):
        """set_apartment_number no characters!"""
        self.assertEqual(self.house.get_apartment_number(), 82)

        self.house.set_apartment_number('a')
        self.assertEqual(self.house.get_apartment_number(), 82)

    def test_set_square_ft(self):
        """set_square_ft Method!"""
        self.assertEqual(self.house.get_square_ft(), 78)

        self.house.set_square_ft(2)
        self.assertEqual(self.house.get_square_ft(), 2)

    def test_not_set_negative_floats_as_square_ft(self):
        """set_square_ft no negative floats!"""
        self.assertEqual(self.house.get_square_ft(), 78)

        self.house.set_square_ft(-2.5)
        self.assertEqual(self.house.get_square_ft(), 78)

    def test_not_set_characters_as_square_ft(self):
        """set_square_ft no characters!"""
        self.assertEqual(self.house.get_square_ft(), 78)

        self.house.set_square_ft('@')
        self.assertEqual(self.house.get_square_ft(), 78)

    def test_str(self):
        """str Method!"""
        self.assertIn(self.house.get_street(), str(self.house))
        self.assertIn(str(self.house.get_apartment_number()), str(self.house))

    def test_find_buildings_with_number_of_rooms(self):
        """find_buildings_with_number_of_rooms Method!"""
        self.assertEqual(House.find_buildings_with_number_of_rooms(self.buildings, 3),
                         [self.buildings[0], self.buildings[3]])

    def test_find_buildings_on_the_floor_with_room_number(self):
        """find_buildings_on_the_floor_with_room_number Method!"""
        self.assertEqual(House.find_buildings_on_the_floor_with_room_number(self.buildings, 3, 9, 10), [])
        self.assertEqual(House.find_buildings_on_the_floor_with_room_number(self.buildings, 3, 8, 10),
                         [self.buildings[3]])


if __name__ == '__main__':
    unittest.main()
