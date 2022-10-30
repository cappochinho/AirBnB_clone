#!/usr/bin/env python3
# Contains the Amenity model that inherits from BaseModel

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Models the amenities in the HBNB facilities"""
    name: str = ''