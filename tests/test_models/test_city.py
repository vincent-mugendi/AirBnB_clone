#!/usr/bin/python3
"""
Unit Test for City Class
"""
import unittest
from datetime import datetime
from models.city import City

class TestCityMethods(unittest.TestCase):
    """Class for testing City methods"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing City Class .......')
        print('.................................\n\n')

    def setUp(self):
        """Set up a clean state before each test"""
        self.city = City()

    def test_instantiation(self):
        """Test if City is properly instantiated"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_to_string(self):
        """Test if City is properly casted to string"""
        my_str = str(self.city)
        my_list = ['City', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_save_method(self):
        """Test if save() method updates updated_at attribute"""
        old_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict() method returns a dictionary"""
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_from_dict_method(self):
        """Test if from_dict() method creates an instance from a dictionary"""
        obj_dict = {
            "__class__": "City",
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000000",
            "updated_at": "2023-01-01T00:00:00.000000",
            "state_id": "456",
            "name": "Test City"
        }
        new_instance = City.from_dict(obj_dict)
        self.assertIsInstance(new_instance, City)
        self.assertEqual(new_instance.id, "123")
        self.assertEqual(new_instance.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.updated_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.state_id, "456")
        self.assertEqual(new_instance.name, "Test City")

if __name__ == '__main__':
    unittest.main()
