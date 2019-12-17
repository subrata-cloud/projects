"""
* Create a class called `Point` which has two instance variables,
`x` and `y` that represent the `x` and `y` co-ordinates respectively. 

* Initialize these instance variables in the `__init__` method

* Define a method, `distance` on `Point` which accepts another `Point` object as an argument and 
returns the distance between the two points.
"""

import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,outer):
        s1=abs(self.x-outer.x)**2
        s2=abs(self.y-outer.y)**2
        dst=math.sqrt(s1+s2)
        return dst
        
