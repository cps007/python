"""
Christian Perigault
July 9, 2020

A module for the 2D Points
"""

import math

class Point:
    """A 2D point."""

    def __init__(self,x=0,y=0,rho=None,theta=None):
        """A new point.
        
        Default is (0,0).
        Use (rho= number, theta = number), for polar coordinates.ArithmeticError
        
        """
        if rho == None:
            self.x = x
            self.y = y
        else:
            self.x = rho * math.cos(theta)
            self.y = rho * math.sin(theta)

    def __str__(self):
        """As string (x,y)"""
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __getitem__(self, key):
        """Accesor for point.x and point.y"""
        if key == "x":
            return self.x
        elif key == "y":
            return self.y

    def __add__(self,point):
        """point1 + point2"""

        return Point(self.x + point.x, self.y + point.y)

    def __mulp__(self,number):
        """point * number"""
        return Point(self.x * number, self.y * number)

    def __truediv__(self,number):
        """point / number"""
        return Point(self.x/number, self.y /number)
