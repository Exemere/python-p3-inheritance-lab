#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    

    def teach(self,knowledge):
        self.knowledge=knowledge
        random_index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[random_index]
