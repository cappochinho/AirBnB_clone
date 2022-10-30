#!/usr/bin/python3
# This module contains the BaseModel (class)
# for the AirBnB clone

from datetime import datetime
import uuid


class BaseModel:
    """BaseModel for all other related classes"""
    def __init__(self, *args, **kwargs):
        """init file"""
        from models.__init__ import storage
        if kwargs:
            kwargs['created_at'] = datetime.now().isoformat()
            kwargs['updated_at'] = datetime.now().isoformat()

            del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints a string representation"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
        # return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the time the object is updated"""
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all the keys/values"""
        new_dict = {}
        new_dict.update(self.__dict__)
        # class_dict = {'__class__': __class__.__name__}
        class_dict = {'__class__':
                               (str(type(self)).split('.')[-1]).split('\'')[0]}
        new_dict.update(class_dict)
        new_dict['created_at'] = datetime.now().isoformat()
        new_dict['updated_at'] = datetime.now().isoformat()
        return new_dict
