#!/usr/bin/python3
"""
This module defines the Amenity class, inheriting from BaseModel
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
	"""
	Amenity class that inherits from BaseModel
	"""
	name = ""

	def __init__(self, *args, **kwargs):
		"""
		Initializes Amenity instance
		"""
		super().__init__(*args, **kwargs)
