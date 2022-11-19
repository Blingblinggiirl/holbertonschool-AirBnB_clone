#!/usr/bin/python3
"""create class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
