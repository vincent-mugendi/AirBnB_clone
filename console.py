#!/usr/bin/python3
"""The console module."""
import cmd
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """The command interpreter class."""
    
    prompt = "(hbnb) "
    
    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, obj_id = arg.split(' ')
            obj_key = "{}.{}".format(class_name, obj_id)
            print(storage.all()[obj_key])
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, obj_id = arg.split(' ')
            obj_key = "{}.{}".format(class_name, obj_id)
            del storage.all()[obj_key]
            storage.save()
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = storage.all()
        if arg:
            try:
                class_name = eval(arg).__name__
                objs = {k: v for k, v in objs.items() if class_name in k}
            except NameError:
                print("** class doesn't exist **")
                return
        print([str(v) for v in objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = eval(args[0]).__name__
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj_instance = storage.all()[obj_key]
        setattr(obj_instance, attr_name, eval(attr_value))
        obj_instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
