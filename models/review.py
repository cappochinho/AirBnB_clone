#!/usr/bin/env python3
# Contains the Review model that inherits from BaseModel

from models.base_model import BaseModel


class Review(BaseModel):
    """Models the reviews that users will leave after using
       an HBNB facility    
    """
    place_id: str = ''
    user_id: str = ''
    text: str = ''