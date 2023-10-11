#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
	"""
	Base class for other classes

	Attributes:
	id (str): A unique identifier for the instance
	created_at (datetime): Timestamp for instance creation
	updated_at (datetime): Timestamp for instance update
	"""

	def __init__(self):
		"""
		Initializes new instance of the BaseModel class
		"""
		self.id = str(uuid.uuid4()) # Generete a new ID and convert it to a string
		self.created_at = datetime.now() # Set created_at attribute with the current date and time
		self.updated_at = datetime.now() # Set upadated_at attributewith the current date

	def __str__(self):
		"""
		Returns a string representation of the object
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""
		Updates the updated_at attribute with the current datetime
		"""
		self.updated_at = datetime.now() # updates the update_at attribute with current datetime

	def to_dict(self):
		"""
		Converts the object attributes to a dictionary

		Returns:
		dict: Dictionary containing object attributes.
		"""
		obj_dict = self.__dict__.copy()
		obj_dict['__class__'] = self.__class__.__name__
		obj_dict['created_at'] = self.created_at.isoformat()
		obj_dict['updated_at'] = self.updated_at.isoformat()
		return obj_dict
