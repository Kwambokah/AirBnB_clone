#!/usr/bin/python3
"""Module for FileStorage class."""
from datetime import datetime
import json
import os


class FileStorage:
    """This class is for storing and retrieving data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores a new object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """This deserializes the JSON file to objects if the file exists"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

                model_classes = self.classes()

                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in model_classes:
                        self.__objects[key] = model_classes[class_name](**val)
        except (FileNotFoundError):
            pass

    def find_all(self, model=""):
        """Find all instances of a specific model"""
        instances = self.__objects.values()

        if model:
            if model in self.classes():
                instances = [obj for obj in instances
                             if isinstance(obj, self.classes()[model])]
            else:
                raise NameError(f"** class '{model}' doesn't exist **")

        return list(instances)

    def find_by_id(self, model, obj_id):
        """Find and return an element of model by its id"""
        classes = self.classes()
        if model not in classes:
            raise NameError(model)

        key = f"{model}.{obj_id}"
        if key not in self.__objects:
            raise NameError(obj_id, model)

        return self.__objects[key]

    def delete_by_id(self, model, obj_id):
        """Delete an element of model by its id"""
        classes = self.classes()
        if model not in classes:
            raise NameError(model)

        key = f"{model}.{obj_id}"
        if key not in self.__objects:
            raise NameError(obj_id, model)

        del self.__objects[key]
        self.save()

    def update_one(self, model, obj_id, field, value):
        """Updates an instance"""
        if model not in self.classes():
            raise NameError(model)

        key = f"{model}.{obj_id}"
        if key not in self.__objects:
            raise NameError(obj_id, model)

        instance = self.__objects[key]
        if field not in ("id", "updated_at", "created_at"):
            setattr(instance, field,
                    type(getattr(instance, field))(value))
            instance.updated_at = datetime.utcnow()
