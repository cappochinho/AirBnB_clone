#!/usr/bin/python3
# Contains the class FileStorage for storing data
# using files


import json

class FileStorage():
    """Serializes instances to a JSON file
       Deserializes JSON file to instances
    """
    __file_path:str = "file.json"
    __objects: dict = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Creates a new object in __objects"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from base_model import BaseModel
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.loads(f.read())
                temp = json.load(f)
                for key, val in temp.items():
                    FileStorage.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass
            