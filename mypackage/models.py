# -*- coding: utf-8 -*-
__all__ = ['Person']


class Person(object):
    def __init__(self, age=None, name=None):
        # 
      self.age = age

        # 
      self.name = name

  
   
    # let's pretend for now we serialize to dict
    def to_dict(self):
        return dict(age=self.age, name=self.name)


    def from_dict(self, data):
        self.age = data.get('age')
        self.name = data.get('name')
          

