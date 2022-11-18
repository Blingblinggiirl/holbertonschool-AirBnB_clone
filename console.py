#!/usr/bin/python3
"""program called console.py that contains the entry point of the
command interpreter"""
from models.base_model import BaseModel
from models import storage
import cmd


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

    def do create(self, arg):
        """create a new instance"""
        args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
