#!/usr/bin/python3
"""
This module defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Base class for all other classes"""

    def __init__(self, *args, **kwargs):
        """ This initializes the public instance attribute"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            storage.new(self)
            return

        for key, val in kwargs.items():
            if key not in ['__class__', 'created_at', 'updated_at']:
                setattr(self, key, val)

        self.created_at = datetime.strptime(
            kwargs.get('created_at', datetime.utcnow().isoformat()),
            '%Y-%m-%dT%H:%M:%S.%f'
        )
        self.updated_at = datetime.strptime(
            kwargs.get('updated_at', datetime.utcnow().isoformat()),
            '%Y-%m-%dT%H:%M:%S.%f'
        )

    def __str__(self):
        """ The string representation of the BaseModel"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates when the attribute was last updated"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of self"""
        i_dict = self.__dict__.copy()
        i_dict["__class__"] = type(self).__name__
        i_dict["name"] = getattr(self, "name", "")
        i_dict["created_at"] = self.created_at.isoformat()
        i_dict["updated_at"] = self.updated_at.isoformat()
        return i_dict
