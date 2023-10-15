#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests for the BaseModel class
    """

    def setUp(self):
        """
        Set up a BaseModel instance for testing.
        """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_object_creation(self):
        """
        Test creation of BaseModel instance and its attributes
        """
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_save_method(self):
        """
        Test the save method to ensure updated_at attribute changes.
        """
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method for proper dictionary generation.
        """
        obj_dict = self.my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('my_number', obj_dict)


if __name__ == "__main__":
    unittest.main()
