#!/usr/bin/python3
"""
Module defines the FileStorage class for serialization and deserialization
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.__file_path = os.path.join(current_directory, "file.json")
        self.__objects = {}

    def all(self):
        """Func Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Func Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Func Deserializes the JSON file to __objects (if the file exists)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
            for key, value in loaded_objects.items():
                class_name = value['__class__']
                obj_id = value['id']
                if class_name == 'BaseModel':
                    obj_instance = BaseModel(**value)
                elif class_name == 'User':
                    obj_instance = User(**value)
                elif class_name == 'State':
                    obj_instance = State(**value)
                elif class_name == 'City':
                    obj_instance = City(**value)
                elif class_name == 'Amenity':
                    obj_instance = Amenity(**value)
                elif class_name == 'Place':
                    obj_instance = Place(**value)
                elif class_name == 'Review':
                    obj_instance = Review(**value)
                else:
                    raise ValueError("Unknown class: {}".format(class_name))
                key = '{}.{}'.format(class_name, obj_id)
                self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass


storage = FileStorage()
storage.reload()
