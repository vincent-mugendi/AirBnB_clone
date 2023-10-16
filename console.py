#!/usr/bin/python3
"""
This module defines the console for the AirBnB clone project.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
storage.CLASSES = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
}


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class
    """
    prompt = "(hbnb) "

    def default(self, line):
        class_name, method = line.split('.')
        if method == "all()":
            self.do_all(class_name)
        else:
            print("*** Unknown syntax: "
                  "{}.{}()".format(class_name, method[:-2]))

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the console at end of file (EOF)
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    def help_quit(self):
        """
        Print help message for the quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Print help message for the EOF command
        """
        print("Exit the console at end of file (EOF)")

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        """
        if not arg:
            print("** class name missing **")
        elif arg not in storage.CLASSES.keys():
            print("** class doesn't exist **")
        else:
            new_instance = storage.CLASSES[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.CLASSES.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and ID
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.CLASSES.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, class_name):
        """
        Print all string representations of instances using <class name>.all()
        """
        class_instances = []
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
        else:
            instances = [
                obj
                for obj in storage.all().values()
                if isinstance(obj, storage.CLASSES[class_name])
            ]
            print([str(obj) for obj in instances])

    def do_update(self, arg):
        """
        Update an instance based on class name and ID
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.CLASSES.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                value = args[3][1:-1] if args[3][0] == '"' else args[3]
                setattr(objects[key], args[2], value)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
