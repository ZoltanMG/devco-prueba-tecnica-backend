#!/usr/bin/python3
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

