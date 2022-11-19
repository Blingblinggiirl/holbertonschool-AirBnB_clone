#!/usr/bin/python3
"""Program called console.py that contains the entry point of the
command interpreter"""
from models.base_model import BaseModel
from models import storage
import cmd
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

dictionary = {"Amenity": Amenity,
              "BaseModel": BaseModel,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State,
              "User": User}


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
