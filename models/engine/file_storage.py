#!/usr/bin/python3
"""serialization-deserialization"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dic_new = {}
        for key in self.__objects.key():
            dic_new[key] = self.__objects.key().to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(dic_new))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dic = json.loads(f)
                for key, value in dic.items():
                    self._objects[key] = eval(value["class_"])(**value)
