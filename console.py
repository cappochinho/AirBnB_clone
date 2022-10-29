#!/usr/bin/env python3
# Contains the entry point of the command intepreter
# Uses the cmd module


import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """CLI for controlling the HBNB console
       Contains custom quit and EOF implementations
       Also implements 'help' just as other shells
    """
    prompt: str = "(hbnb)"

    def do_quit(self, arg):
        """Command to exit the running program"""
        sys.exit(1)

    def do_EOF(self, arg):
        """Implements the end-of-file keyboard combination
           (Ctrl + D)
        """
        return True

    def do_help(self, line):
        if line == 'quit':
            print('Quit command to exit the program')

        elif line == 'EOF':
            print('End-Of-File(Ctrl-D), works like the quit command')

        elif line == 'create':
            print('Creates a new instance of the object')

        elif line == 'show':
            print("Prints the string representation of a class instance")

        elif line == 'destroy':
            print("Deletes an instance based on the class name and id")

        elif line == 'update':
            print("Updates an instance based on the class name and id")

        else:
            print(
                "Documented commands (type help < topic >):\n",
                "========================================\n",
                "EOF  help  quit create show destroy update"
                )

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        if not arg:
            print("** class name missing **")
            return

        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        
        new_instance = BaseModel()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, args):
        """Prints the string representation of a class instance"""

        args = args.partition(" ")
        
        if not args[0]:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if not args[1]:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]

        try:
            print(storage.__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

        args = args.partition(" ")

        if not args[0]:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if not args[1]:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances"""

        if args != "BaseModel":
            print("** class doesn't exist **")
            return

        for value in storage.__objects.values():
           print(value)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = args.partition(" ")
        
        if not args:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if not args[1]:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]

        try:
            if key not in storage.all():
                print("** no instance found **")
        except KeyError:
            pass

        if not args[2]:
            print("** attribute name missing **")
            return

        try:
            if args[2] not in storage.all():
                print("** attribute name missing **")
                return
        except AttributeError:
            pass

        if not args[3]:
            print("** value missing **")
            return

        if args[3] in ["id", "created_at", "updated_at"]:
            return

        if args[4]:
            return




if __name__ == '__main__':
    HBNBCommand().cmdloop()