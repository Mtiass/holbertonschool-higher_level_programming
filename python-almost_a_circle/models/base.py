#!/usr/bin/python3
"""
This module defines Base as a class.
"""
import json


class Base:
    """
    This is a class that works as a base for other classes.

    Attributes:
        nb_objects: is a private class attribute.

        id: is a public instance attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initialization method.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This is a static method that returns the JSON string
        representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This is a class method that writes the JSON string
        representation of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []
        listdicts = []
        for obj in list_objs:
            objdic = obj.to_dictionary()
            listdicts.append(objdic)
        flname = cls.__name__ + '.json'
        with open(flname, 'w', encoding="utf-8") as file:
            lstojson = cls.to_json_string(listdicts)
            file.write(lstojson)

    @staticmethod
    def from_json_string(json_string):
        """
        This is a static method that returns the list of the JSON
        string representation json_string.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This is a class method that returns an instance with all
        attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        This is a class method that returns a list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                dicslist = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        instces = []
        for dict_obj in dicslist:
            instance = cls.create(**dict_obj)
            instces.append(instance)
        return instces
