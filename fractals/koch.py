# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:17:45 2020

@author: cperigault

Koch curve fractal.

"""

from turtle import Turtle
from math import pi
from tqdm import tqdm


def koch(n=4):
    """Draw koch curve fractal

    Draw the Koch fractal using Python turtle graphics.
    
    :param n: Levels of recursive division to draw fractal.
    :type  n: int.
    """
    angles = [0,60,-120,60]
    
    def draw(level,angle):
        """Draw a segment of Koch curve"""
        nonlocal turtle
        turtle.turn(angle)
   
        if level == 0:
            turtle.forward()
            #print(turtle.pos())
            bar.update(1)
        else:
            for i in range(4):
                turtle.resize(1/3)
                draw(level-1, angles[i])
                turtle.resize(3)
    # Initialize screen
    turtle = Turtle(w=1000,h=500)
    canvas_w = 1000
    # Initialize turtle
    turtle.goto(25,25)
    turtle.step(canvas_w-50)
    
    #print(turtle.pos())
    # Fractal
    bar = tqdm(total=4**n)
    draw(n,0)
    turtle.save("koch")

if __name__ == "__main__":
     print("\n\nDrawing Koch curve.\n ")
     koch(5)
     print ("\n\nDone")