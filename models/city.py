#!/usr/bin/python3

"""This file defines the City Model
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The class for City Model"""

    name: str = ""
    state_id: str = ""
