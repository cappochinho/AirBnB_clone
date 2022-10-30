#!/usr/bin/env python3
# Contains the State model that inherits from BaseModel

from models.base_model import BaseModel


class State(BaseModel):
    """Models that State an HBNB is enlisted in"""
    name:str = ''