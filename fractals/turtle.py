# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:17:45 2020

@author: cperigault 
"""
import math
from PIL import Image, ImageDraw

class Turtle():
    """Turtle graphic object.
    
    """
    def __init__(self,w=1_000,h=1_000, radians = False, canvas_color = 'White', color = 'black'):
        """Create a new turtle instance.
        
        w,h: canvas size for drawing.
        canvas_color: the canvas background color.
        color: turtle drawing color.
        
        Turtle initial position is at (0,0)
        """
        self.w = w
        self.h = h
        self.img  = Image.new("RGB", (w, h), color = canvas_color)
        self.draw = ImageDraw.Draw(self.img)
        self.x = 0
        self.y = 0
        self.angle = 0
        self.step_size = 1
        self.is_down  = True
        self.color = color
        if radians:
            self.angle_to_radians = 1.0
        else:
            self.angle_to_radians = math.pi/180.0
    
    def pos(self):
        """Return current turtle position (x,y)"""
        return (self.x,self.y)
    
    def goto(self,x,y):
        """Set turtle position at (x,y)"""
        self.x = x
        self.y = y
    def forward(self):
        """Draw a line of lengt step*step_size"""
        # print( "(" + str(int(self.x)) + "," + str(int(self.y)) + ")", end='')

        point_x = round(self.x + self.step_size * math.cos(self.angle*self.angle_to_radians))
        point_y = round(self.y + self.step_size * math.sin(self.angle*self.angle_to_radians))
        # print( "-> (" + str(int(point_x)) + "," + str(int(point_y)) + ")")
        if self.is_down:
            self.draw.line((self.x,self.h-self.y,point_x,self.h-point_y), fill = self.color)
        self.x = point_x
        self.y = point_y
        
        
    def step(self,size):
        """Step size in pixels for drawing."""
        self.step_size = size

    def resize(self,factor):
        """Step size in pixels for drawing."""
        self.step_size = self.step_size * factor
    
    def turn(self,angle):
        """Set turtle angle for drawing."""
        self.angle = self.angle + angle
    
    def down(self):
        """Draw"""
        self.is_down = True
    
    def up(self):
        """Do not draw"""
        self.is_down = False
        
    def save(self,file_name): 
        """Save imageas a png file."""
        self.img.save(file_name + ".png","PNG")
    
    
if __name__ == "__main__":
    #Draw a square
    
    # Move to (25,25)
    print("Move to (25,25)")
    turtle = Turtle()
    turtle.up()
    turtle.step(25)
    turtle.forward()
    turtle.turn(90)
    turtle.forward()
    turtle.turn(-90)
    turtle.down()
    # Draw
    print("Drawing rectangle")
    turtle.step(400)
    turtle.forward()
    turtle.turn(90)
    turtle.forward()
    turtle.turn(90)
    turtle.forward()
    turtle.turn(90)
    turtle.forward()
    turtle.turn(90)
    turtle.forward()
    turtle.save("turtle_test")
    
    
    