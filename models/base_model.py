#!/usr/bin/python3
"""base class"""
import json
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ This will be define all common attributes/methods 
    for other classes """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value 
                elif key == __class__:
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """ This will be return a dictionary that contains
        key and values in __dic__ of the instance """
        dicnew = self.__dict__.copy()
        dicnew["created_at"] = self.created_at.isoformat()
        dicnew["updated_at"] = self.updated_at.isoformat()
        dicnew["__class__"] = self.__class__.__name__
        return dicnew
    
    def save(self):
        """ this is useful when you update and has the current time """
        self.udated_at = datetime.now()

    def __str__(self):
        """ String rep of the model """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
