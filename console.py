#!/usr/bin/env python3
# Contains the entry point of the command intepreter
# Uses the cmd module


import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """CLI for controlling the HBNB console
       Contains custom quit and EOF implementations
       Also implements 'help' just as other shells
    """
    prompt: str = "(hbnb)"

    model_list = {"BaseModel": BaseModel, "User": User}

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

        if arg not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return
        
        new_instance = HBNBCommand.model_list[arg]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, args):
        """Prints the string representation of a class instance"""

        args = args.partition(" ")
        model_name = args[0]
        model_id = args[2]
        
        if not model_name:
            print("** class name missing **")
            return

        if model_name not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return

        if not model_id:
            print("** instance id missing **")
            return

        key = model_name + '.' + model_id

        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

        args = args.split(" ")

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
        all_list = []
        
        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.model_list:
                print("** class doesn't exist **")
                return

            for key, value in storage._FileStorage__objects.items():
                if key.split('.')[0] == args:
                    all_list.append(str(value))

        else:
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))

        print(all_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        model_name = model_id = attr_name = attr_val = kwargs = ''

        args = args.partition(" ")
        
        if not args:
            print("** class name missing **")
            return
        else:
            model_name = args[0]

        if model_name not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            model_id = args[0]
        else:
            print("** instance id missing **")
            return

        key = model_name + '.' + model_id

        if key not in storage.all():
            print("** no instance found **")

        # determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for key, value in kwargs.items():
                args.append(key)
                args.append(value)
        else: # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                attr_name = args[1: second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if attr_name argument was not quoted
            if not attr_name and args[0] != ' ':
                attr_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                attr_val = args[2][1: args[2].find('\"', 1)]

            # if attr_val was not quoted
            if not attr_val and args[2]:
                attr_val = args[2].partition(' ')[0]

            args = [attr_name, attr_val]

        new_store = storage.all()[key]

        for i, attr_name in enumerate(args):
                # block only runs on even iterations
            if (i % 2 == 0):
                attr_val = args[i + 1]  # following item is value
                if not attr_name:  # check for attr_name
                    print("** attribute name missing **")
                    return
                if not attr_val:  # check for attr_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if attr_name in HBNBCommand.types:
                    attr_val = HBNBCommand.types[attr_name](attr_val)

                # update dictionary with name, value pair
                new_store.__dict__.update({attr_name: attr_val})

            new_store.__dict__.update({attr_name: attr_val})

        new_store.save()
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()