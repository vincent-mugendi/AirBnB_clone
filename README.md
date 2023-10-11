# AirBnB clone - The console
!{https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231011%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231011T062411Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8cc3a5125935d8b855359e720e9d3b14eb255f010fcdc1bfc89a525b43422615}
---
## This is an Alx Team project that involves creating a simplified version of the AirBnB web application
---
###PROJECT DESCRIPTION
This team project is the first step in the ALX Software Engineer program towards building a full-stack AirBnB clone web application. It involves developing a custom command-line interface (console.py) for managing data in a database, as well as the base classes for storing and managing the data. The console.py will enable users to perform CRUD operations on data and other common data management tasks, while the base classes will provide a common interface for all data objects in the system.


https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231010T051036Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a9c33693aad500ce85ac202dd65f157197679ebad71ac21607043b20b01d2391
1. a class BaseModel that defines all common attributes/methods for other classes: (models/base_model.py)
 Public instance attributes:
id: string - assign with an uuid when an instance is created:
you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public instance attribute updated_at with the current datetime
to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class name of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
2. Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
Update models/base_model.py:

__init__(self, *args, **kwargs):
you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
*args won’t be used
if kwargs is not empty:
each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
each value of this dictionary is the value of this attribute name
Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
otherwise:
create id and created_at as you did previously (new instance) 
