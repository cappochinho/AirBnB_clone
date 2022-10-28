#!/usr/bin/env python3
# Contains the entry point of the command intepreter
# Uses the cmd module


import cmd
import sys


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

    def do_help(self, *line):
        if line[0] == 'quit':
            print('Quit command to exit the program')
        elif line[0] == 'EOF':
            print('End-Of-File(Ctrl-D), works like the quit command')
        elif line[0] == 'create':
            print('Creates a new instance of the object')
        else:
            print("Documented commands (type help < topic >):\n========================================\nEOF  help  quit")

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        from models.base_model import BaseModel
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        elif not arg:
            print("** class name missing **")
            return
        
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)
        




if __name__ == '__main__':
    HBNBCommand().cmdloop()