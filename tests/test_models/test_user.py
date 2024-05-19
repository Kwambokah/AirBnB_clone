#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import os
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Test cases for the User model."""

    def setUp(self):
        """Set up the test environment."""
        self.user = User()

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_user_inherits_from_base_model(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_instance_creation(self):
        """Test the instantiation of the User class."""
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_attributes(self):
        """Test default attribute values."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        """Test the string representation of User instances."""
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()
