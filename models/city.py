#!/usr/bin/env python3
# Contains the City model that inherits from BaseModel

from models.base_model import BaseModel
from models.state import State


class City(State, BaseModel):
    """Models the city an HBNB is listed in"""
    state_id: str = ''
    name: str = ''
