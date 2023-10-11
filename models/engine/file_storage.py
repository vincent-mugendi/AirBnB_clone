#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from os.path import exists
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        obj = BaseModel(**value)
                    elif class_name == 'State':
                        obj = State(**value)
                    elif class_name == 'City':
                        obj = City(**value)
                    elif class_name == 'Amenity':
                        obj = Amenity(**value)
                    elif class_name == 'Place':
                        obj = Place(**value)
                    elif class_name == 'Review':
                        obj = Review(**value)
                    FileStorage.__objects[key] = obj
