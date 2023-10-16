#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
# run_tests.py

import sys
import unittest
from datetime import datetime
from models.base_model import BaseModel

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestBaseModelMethods(unittest.TestCase):
    """Class for testing BaseModel methods"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('... Testing BaseModel Class ....')
        print('.................................\n\n')

    def setUp(self):
        """Set up a clean state before each test"""
        self.base_model = BaseModel()

    def test_instantiation(self):
        """Test if BaseModel is properly instantiated"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_string(self):
        """Test if BaseModel is properly casted to string"""
        my_str = str(self.base_model)
        my_list = ['BaseModel', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_save_method(self):
        """Test if save() method updates updated_at attribute"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict() method returns a dictionary"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_from_dict_method(self):
        """Test if from_dict() method creates an instance from a dictionary"""
        obj_dict = {
            "__class__": "BaseModel",
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000000",
            "updated_at": "2023-01-01T00:00:00.000000"
        }
        new_instance = BaseModel.from_dict(obj_dict)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(new_instance.id, "123")
        self.assertEqual(new_instance.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.updated_at, datetime(2023, 1, 1))


if __name__ == '__main__':
    unittest.main()
