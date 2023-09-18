#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.knowledge = []
    
    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)
        pass
    