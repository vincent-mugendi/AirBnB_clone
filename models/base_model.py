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
            **kwargs: Arbitrary keyword arguments to create the instance
        """
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self) -> str:
        """
        Converts the object to a string
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self) -> None:
        """
        Sets the updated_at attribute to the current datetime
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Function Serializes the object to a dictionary.
        """
        obj_dict = self.__dict__.copy()

        # convert the 'created_at and updated_at attributes to ISO format
        obj_dict["created_at"] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f'
        )
        obj_dict["updated_at"] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f'
        )

        # Add the __class__ attributes to the dictionary
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Creates an instance of the class from a dictionary representation.
        Args:
            obj_dict (dict): Dictionary containing object attrib
        Returns:
            cls: Instance of the class.
        """
        class_name = obj_dict.pop("__class__", cls.__name__)
        obj_dict["created_at"] = datetime.strptime(
            obj_dict["created_at"], '%Y-%m-%dT%H:%M:%S.%f'
        )
        obj_dict["updated_at"] = datetime.strptime(
            obj_dict["updated_at"], '%Y-%m-%dT%H:%M:%S.%f'
        )
        return cls(__class__=class_name, **obj_dict)
