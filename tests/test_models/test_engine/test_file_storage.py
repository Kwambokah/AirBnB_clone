#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from models.city import City
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Reset the storage to the initial state."""
        storage.reload()
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_file_storage_all(self):
        """Test the all() method of FileStorage."""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_file_storage_new(self):
        """Test the new() method of FileStorage."""
        user = User()
        self.storage.new(user)
        objects = self.storage.all()
        self.assertIn(f"User.{user.id}", objects)

    def test_file_storage_save(self):
        """Test the save() method of FileStorage."""
        user = User()
        self.storage.new(user)
        self.storage.save()

        # Check if the file exists
        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path), "File not created after save()")

        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Add assertions to check the content
        self.assertIn(user.id, content, "User ID not found in file")
        user_data = user.to_dict()
        user_data_json = json.dumps(user_data)  # Convert to JSON
        self.assertIn(user_data_json, content, "User data not found in file")

    def test_file_storage_reload(self):
        """Test the reload() method of FileStorage."""
        user = User()
        self.storage.new(user)
        self.storage.save()

        # Reload the storage
        self.storage.reload()

        objects = self.storage.all()
        self.assertIn(f"User.{user.id}", objects)


if __name__ == "__main__":
    unittest.main()
