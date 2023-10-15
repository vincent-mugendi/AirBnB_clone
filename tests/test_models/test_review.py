#!/usr/bin/python3
"""
Unit Test for Review Class
"""
import unittest
from datetime import datetime
from models.review import Review

class TestReviewMethods(unittest.TestCase):
    """Class for testing Review methods"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Review Class .......')
        print('.................................\n\n')

    def setUp(self):
        """Set up a clean state before each test"""
        self.review = Review()

    def test_instantiation(self):
        """Test if Review is properly instantiated"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_to_string(self):
        """Test if Review is properly casted to string"""
        my_str = str(self.review)
        my_list = ['Review', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_save_method(self):
        """Test if save() method updates updated_at attribute"""
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict() method returns a dictionary"""
        obj_dict = self.review.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_from_dict_method(self):
        """Test if from_dict() method creates an instance from a dictionary"""
        obj_dict = {
            "__class__": "Review",
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000000",
            "updated_at": "2023-01-01T00:00:00.000000",
            "place_id": "456",
            "user_id": "789",
            "text": "This is a test review"
        }
        new_instance = Review.from_dict(obj_dict)
        self.assertIsInstance(new_instance, Review)
        self.assertEqual(new_instance.id, "123")
        self.assertEqual(new_instance.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.updated_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.place_id, "456")
        self.assertEqual(new_instance.user_id, "789")
        self.assertEqual(new_instance.text, "This is a test review")

if __name__ == '__main__':
    unittest.main()
