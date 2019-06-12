#!/usr/bin/python3
"""
base.py contains base class 
"""
import json


class Base:
    """
        base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return: json representation of list_dictionaries """
        return json.dumps(list_dictionaries) if list_dictionaries is not None else "[]"

    @staticmethod
    def from_json_string(json_string):
        """ Return: list of json rep """
        return json.loads(json_string) if json_string is not None else []
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string to a rep of list_objs """
        newList=[]
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for objt in list_objs:
                newList.append(objt.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(newList))
    
    @classmethod
    def create(cls, **dictionary):
        """ returns instance with attri set up """
        fReturn = cls(1, 1)
        fReturn.update(**dictionary)
        return fReturn
    
    @classmethod
    def load_from_file(cls):
        """ """
        try:
            with open('{}.json' .format(cls.__name__), 'r') as f:
                newDictionary = cls.from_json_string(f.read())
        except IOError:
            return []
        return [cls.create(**idx) for idx in newDictionary]
    


