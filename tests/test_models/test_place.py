#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
import os
from datetime import datetime
from models.place import Place
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ test cases for place """

    def setUp(self):
        """ set up tests """
        self.place = Place()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_place_inherits_from_base_model(self):
        """ test place if it inherits from basemodel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes(self):
        """ test the attributes of place"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_place_attributes_assignment(self):
        """test attribute assignmmennts of place"""
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Test Place"
        self.place.description = "A description"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = ["wifi", "pool"]
        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "456")
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "A description")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["wifi", "pool"])

    """
    def test_place_to_dict_method(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)
    """
    def test_place_str_representation(self):
        """ test str representation"""
        self.assertEqual(str(self.place), "[Place] ({}) {}"
                         .format(self.place.id, self.place.__dict__))


if __name__ == '__main__':
    unittest.main()
