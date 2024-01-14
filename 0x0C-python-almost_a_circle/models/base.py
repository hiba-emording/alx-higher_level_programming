#!/usr/bin/python3
"""
Defines Base Class

Manages id attr in all subclasses
"""
from json import *
from csv import *


class Base:
    """ Represents a class: Basic """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        file_name = "{}.json".format(cls.__name__)
        object_list = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, 'w') as f:
            f.write(cls.to_json_string(object_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return "[]"
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dictionary_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """a function for serialiazation in CVS"""
        file_name = "{}.csv".format(cls.__name__)
        print("Saving to file:", file_name)

        with open(file_name, 'w', newline='') as f:
            csv_writer = writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """a function for deserialiazation in CVS"""
        file_name = "{}.csv".format(cls.__name__)

        try:
            with open(file_name, 'r', newline='') as f:
                csv_reader = reader(f)
                instances = []
                for row in csv_reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls.create(
                                id=int(row[0]),
                                width=int(row[1]),
                                height=int(row[2]),
                                x=int(row[3]),
                                y=int(row[4])
                                )
                    elif cls.__name__ == "Square":
                        obj = cls.create(
                                id=int(row[0]),
                                size=int(row[1]),
                                x=int(row[2]),
                                y=int(row[3])
                                )
                    instances.append(obj)
                return instances
        except IOError:
            return []
