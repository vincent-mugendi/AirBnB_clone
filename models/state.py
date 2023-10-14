#!/usr/bin/python3
"""
This module defines the State class, inheriting from BaseMode
"""

from models.base_model import BaseModel

class State(BaseModel):
	"""
	State class that inherits from BaseModel
	"""
	name = ""

	def __init__(self, *args, **kwargs):
		"""
		Initializes State instance
		"""
		super().__init__(*args, **kwargs)
