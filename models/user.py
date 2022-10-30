#!/usr/bin/env python3
# Contains the Class User which contains the user's information


from models.base_model import BaseModel


class User(BaseModel):
    """Manages the data of the user of HBNB"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
