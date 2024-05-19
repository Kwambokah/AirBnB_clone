#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import time
import re
import json


class TestState(unittest.TestCase):
    """Test cases for the State model."""

    def setUp(self):
        """Set up the test environment."""
        self.state = State()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()

    def resetStorage(self):
        """Test that Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_state_inherits_from_base_model(self):
        """Test inheritance from basemodel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_instance_creation(self):
        """Test the instantiation of the State class."""
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_str_representation(self):
        """Test the string representation of State instances."""
        expected_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_str)

    def test_name_default_value(self):
        """Test the default value of the 'name' attribute."""
        self.assertEqual(self.state.name, "")

    def test_to_dict_method(self):
        """Test the to_dict method of State instances."""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], self.state.name)


if __name__ == "__main__":
    unittest.main()
