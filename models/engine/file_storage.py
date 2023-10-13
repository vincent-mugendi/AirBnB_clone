#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Returns the dictionary __objects"""
		return self.__objects

	def new(self, obj):
		"""Sets in __objects the obj with key <obj class name>.id"""
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		self.__objects[key] = obj

	def save(self):
		"""Serializes __objects to the JSON file (path: __file_path)"""
		serialized_objects = {}
		for key, obj in self.__objects.items():
			serialized_objects[key] = obj.to_dict()

		with open(self.__file_path, "w") as json_file:
			json.dump(serialized_objects, json_file)

	def reload(self):
		"""Deserializes the JSON file to __objects (if the file exists)"""
		try:
			with open(self.__file_path, "r") as json_file:
				loaded_objects = json.load(json_file)
				for key, obj_dict in loaded_objects.items():
					class_name, obj_id = key.split('.')
					obj_instance = BaseModel.from_dict(obj_dict)
					self.__objects[key] = obj_instance
		except FileNotFoundError:
			pass

storage = FileStorage()
storage.reload()
