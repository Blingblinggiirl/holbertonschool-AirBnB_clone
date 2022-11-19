#!/usr/bin/python3
"""program called console.py that contains the entry point of the
command interpreter"""
from models.base_model import BaseModel
from models import storage
import cmd
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

dictionary = {"Amenity": Amenity,
              "BaseModel": BaseModel,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State}


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new = eval(args[0])()
            new.save()
            print(new.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id"""
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        dictt = storage.all()
        for key, value in dictt.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    print(value)
                    return
        for j in dictionary.keys():
            if my_args[0] == j:
                print("** no instance found **")
                return
        print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        dictt = storage.all()
        for key, value in dictt.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    all_objects = storage.all()
                    all_objects.pop(key)
                    storage.save()
                    return
        for j in dictionary.keys():
            if my_args[0] == j:
                print("** no instance found **")
                return
        print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the class name"""
        my_arg = arg.split()
        listt = []
        dictt = storage.all()
        if len(arg) == 0:
            for key, value in dictt.items():
                listt.append(str(value))
            print(my_listt)
        else:
            for key, value in my_dictt.items():
                if my_arg[0] == value.__class__.__name__:
                    listt.append(str(value))
            if len(listt) == 0:
                print("** class doesn't exist **")
            else:
                print(listt)

    def do_update(self, args):
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        dictt = storage.all()
        for key, value in dictt.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    if len(my_args) == 2:
                        print("** attribute name missing **")
                        return
                    if len(my_args) == 3:
                        print("** value missing **")
                        return
                    all_objects = storage.all()
                    setattr(all_objects[key], my_args[2], my_args[3])
                    storage.save()
                    return
        for j in dictionary.keys():
            if my_args[0] == j:
                print("** no instance found **")
                return
        print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
