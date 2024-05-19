#!/usr/bin/python3
"""
This module deals with unittests for the console.

"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
import re
import unittest


class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        # Check if quit command exits the program
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_quit(''))
            self.assertEqual(f.getvalue().strip(), '')

    def test_EOF(self):
        # Check if EOF command exits the program
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_EOF(''))
            self.assertEqual(f.getvalue().strip(), '')

    def test_emptyline(self):
        # Check if emptyline method does not produce any output
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue().strip(), '')

    def test_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create UnknownClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_instance(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(re.match(r"^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$",
                            output))

    def test_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy UnknownClass 1234-5678")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_invalid_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel invalid-id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_create_existing_instance(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output1 = f.getvalue().strip()

            self.console.onecmd("create BaseModel")
            output2 = f.getvalue().strip()

            self.assertNotEqual(output1, output2)
            # Ensure that two consecutive creations give different instance IDs

    def test_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create UnknownClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show UnknownClass 1234-5678")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_invalid_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel invalid-id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy UnknownClass 1234-5678")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_invalid_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel invalid-id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")


if __name__ == "__main__":
    import unittest

    unittest.main()
