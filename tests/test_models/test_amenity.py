#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import os
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """sets up tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_amenity_inherits_from_base_model(self):
        """tests inheritance"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """test attr for amenity"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_attributes_default_values(self):
        """test attr default values"""
        self.assertEqual(self.amenity.name, "")

    def test_amenity_attributes_assignment(self):
        """test attr assignment"""
        self.amenity.name = "Gymn"
        self.assertEqual(self.amenity.name, "Gymn")

    def test_amenity_str_representation(self):
        """test str representation"""
        self.assertEqual(str(self.amenity), "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__))


if __name__ == '__main__':
    unittest.main()
