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

	def __init__(self, *args, **kwargs):
		"""
		Initializes new instance of the BaseModel class

		Args:
			*args: Variables length argument list (unused)
			**kwargs: Arbitrary keyword arguments to create the instance from a dictionary representation
		"""

		# Set default values for the `id`, `created_at`, and `updated_at` attributes.
		kwargs.setdefault("id", str(uuid.uuid4()))
		kwargs.setdefault("created_at", datetime.now())
		kwargs.setdefault("updated_at", datetime.now())

		# Set the object attributes.
		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self) -> str:
		"""
		Converts the object to a string
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self) -> None:
		"""
		Sets the updated_at attribute to the current datetime
		"""
		self.updated_at = datetime.now() # updates the update_at attribute with current datetime

	def to_dict(self):
		"""
		Serializes the object to a dictionary.
		"""
		obj_dict = {
			key: value
			for key, value in self.__dict__.items()
			if not key.startswith("__")
		}
		obj_dict["__class__"] = self.__class__.__name__
		return obj_dict
