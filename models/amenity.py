#!/usr/bin/python3
"""Defines the Amenity class."""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity."""
        super().__init__(*args, **kwargs)
