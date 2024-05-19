#!/usr/bin/python3
"""
The console module
"""

import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # Exit commands
    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        pass

    # Create command
    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it,
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            classes = storage.classes()

            if class_name not in classes:
                print("** class doesn't exist **")
            else:
                class_instance = classes[class_name]
                if class_instance:
                    new_instance = class_instance()
                    storage.new(new_instance)
                    storage.save()
                    print(new_instance.id)
                else:
                    print("** class doesn't exist **")

    # Show command
    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]

            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                instance = storage.all().get(key)

                if instance is None:
                    print("** no instance found **")
                else:
                    print(instance)

    # Destroy command
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]

            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    try:
                        storage.delete_by_id(class_name, instance_id)
                    except (NameError, SyntaxError):
                        print("** no instance found **")

    # All command
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        match = re.match(r"^(\w+)\.all\(\)$", arg)

        if match:
            class_name = match.group(1)
            try:
                instances = storage.find_all(class_name)
                print([str(instance) for instance in instances])
            except NameError:
                print("** class doesn't exist **")
        else:
            args = arg.split()
            if not args:
                print("** class name missing **")
            else:
                try:
                    instances = storage.find_all(*args)
                    print([str(instance) for instance in instances])
                except (NameError, SyntaxError):
                    print("** class doesn't exist **")
                except TypeError:
                    print("** invalid arguments **")

    # Update command
    def do_update(self, arg):
        """Updates an instance by adding or updating attribute"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print("** no instance found **")
                return

            instance = storage.find_by_id(class_name, instance_id)
            if not hasattr(instance, attribute_name):
                print("** attribute name missing **")
                return

            try:
                # Assume the attribute value is valid for its type
                # (casting is not needed for string, integer, and float)
                setattr(instance, attribute_name, eval(attribute_value))
                instance.save()
            except (NameError, SyntaxError):
                print("** class doesn't exist **")

    def do_count(self, arg):
        """Counts the instances of a specified class"""
        class_name = arg.split()[0] if arg else None

        if class_name and class_name in storage.classes():
            instances = storage.find_all(class_name)
            print(len(instances))
        else:
            print("** class doesn't exist**")

    def handle_class_methods(self, arg):
        """Handle Class Methods <cls>.all(), <cls>.show() etc"""
        try:
            if arg.endswith('()'):
                arg = arg[:-2]
            class_name, method_name = arg.split('.')
            cls = getattr(storage.classes, class_name)
            if (hasattr(cls, method_name) and
                    callable(getattr(cls, method_name))):
                method = getattr(cls, method_name)
                result = method()
                if result is not None:
                    print(result)
            else:
                print("** invalid method **")
        except AttributeError:
            print("** invalid method **")
        except NameError:
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print(f"** {e} **")

    def default(self, line):
        if line is None:
            return

        cmdPattern = r"^([A-Za-z]+)\.([a-z]+)\(([^()]*)\)"
        paramsPattern = (r'^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*'
                         r'(?:("?[^"]+"?)))?)?')
        m = re.match(cmdPattern, line)

        if not m:
            super().default(line)
            return

        mName, method, params = m.groups()
        m = re.match(paramsPattern, params)
        params = [item for item in m.groups() if item] if m else []

        cmd = " ".join([mName] + params)

        method_functions = {
            'all': self.do_all,
            'count': self.do_count,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
        }

        if method in method_functions:
            return method_functions[method](cmd)
        else:
            super().default(line)


if __name__ == '__main__':
