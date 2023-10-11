#!/usr/bin/python3
"""Defines the Review class."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Review."""
        super().__init__(*args, **kwargs)
