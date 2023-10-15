#!/usr/bin/python3
"""
Unit Test for Amenity Class
"""
import unittest
from datetime import datetime
import models
from models.amenity import Amenity

class TestAmenityMethods(unittest.TestCase):
    """Class for testing Amenity methods"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Amenity Class ....')
        print('.................................\n\n')

    def setUp(self):
        """Set up a clean state before each test"""
        self.amenity = Amenity()

    def test_instantiation(self):
        """Test if Amenity is properly instantiated"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, models.base_model.BaseModel)

    def test_to_string(self):
        """Test if Amenity is properly casted to string"""
        my_str = str(self.amenity)
        my_list = ['Amenity', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """Test if Amenity does not have an updated attribute"""
        my_str = str(self.amenity)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """Test if save() function adds updated_at attribute"""
        self.amenity.save()
        actual = type(self.amenity.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """Test if to_json() returns a serializable dict object"""
        amenity_json = self.amenity.to_json()
        actual = 1
        try:
            serialized = json.dumps(amenity_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """Test if to_json() includes class key with value 'Amenity'"""
        amenity_json = self.amenity.to_json()
        actual = None
        if amenity_json['__class__']:
            actual = amenity_json['__class__']
        expected = 'Amenity'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """Test if Amenity has a 'name' attribute"""
        self.amenity.name = "greatWifi"
        actual = self.amenity.name
        expected = "greatWifi"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
