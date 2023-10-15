#!/usr/bin/python3
"""
Unit Test for Place Class
"""
import unittest
from datetime import datetime
from models.place import Place

class TestPlaceMethods(unittest.TestCase):
    """Class for testing Place methods"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Place Class .......')
        print('.................................\n\n')

    def setUp(self):
        """Set up a clean state before each test"""
        self.place = Place()

    def test_instantiation(self):
        """Test if Place is properly instantiated"""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_to_string(self):
        """Test if Place is properly casted to string"""
        my_str = str(self.place)
        my_list = ['Place', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_save_method(self):
        """Test if save() method updates updated_at attribute"""
        old_updated_at = self.place.updated_at
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict() method returns a dictionary"""
        obj_dict = self.place.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_from_dict_method(self):
        """Test if from_dict() method creates an instance from a dictionary"""
        obj_dict = {
            "__class__": "Place",
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000000",
            "updated_at": "2023-01-01T00:00:00.000000",
            "city_id": "456",
            "user_id": "789",
            "name": "Test Place",
            "description": "This is a test place",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "amenity_ids": ["a1", "a2"]
        }
        new_instance = Place.from_dict(obj_dict)
        self.assertIsInstance(new_instance, Place)
        self.assertEqual(new_instance.id, "123")
        self.assertEqual(new_instance.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.updated_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.city_id, "456")
        self.assertEqual(new_instance.user_id, "789")
        self.assertEqual(new_instance.name, "Test Place")
        self.assertEqual(new_instance.description, "This is a test place")
        self.assertEqual(new_instance.number_rooms, 2)
        self.assertEqual(new_instance.number_bathrooms, 1)
        self.assertEqual(new_instance.max_guest, 4)
        self.assertEqual(new_instance.price_by_night, 100)
        self.assertEqual(new_instance.latitude, 40.7128)
        self.assertEqual(new_instance.longitude, -74.0060)
        self.assertEqual(new_instance.amenity_ids, ["a1", "a2"])

if __name__ == '__main__':
    unittest.main()
