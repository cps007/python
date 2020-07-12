# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:17:45 2020

@author: cperigault
"""

import turtle
from tqdm import tqdm


def sierpinski(n=10):
    """Draw Sierpinkinski fractal
    
    Args:
        n: number of iterations.
    """

    def poly_length(pen, length, angle, step_size):
        """"Draw a poligon with length and angles"""
        for i in range(int(360/angle)):
            pen.forward(length * step_size)
            pen.left(angle)
    
    def draw(pen, level, step_size):
        """Recursively draw a Sierpinsky triangle"""
        if level == 0:
            poly_length(pen, 1 , 360/3, step_size)
        else:
            for i in range(3):
                draw(pen,level - 1,step_size * 1/2) 
                pen.forward(step_size * 1) 
                pen.left(360/3)
                
    # Initialize turtle
    screen = turtle.getscreen()
    my_turtle = turtle.Turtle()
    screen.title("Sierpinski")
    canvasW,canvasH = turtle.screensize()
    print(canvasW,canvasH)
    my_turtle.penup()
    
    my_turtle.goto(-canvasW/2,-canvasH/2)
    
    my_turtle.pendown()
    my_turtle.pencolor("red")
    my_turtle.pensize("1")
    my_turtle.speed(0)
    draw(my_turtle,5,canvasW)
    my_turtle.clearstamps()
    turtle.done()
if __name__ == "__main__":
     print("\n\nDrawing random Sierpinsky triangle.\n ")
     sierpinski()
     print ("Done")