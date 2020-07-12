import random
from point import Point
from PIL import Image, ImageDraw

def sierpinski(n=1_000_000,canvas_size=1_000):
    """Sierpinski fractal triangle, with random ifs.
    
    n: iterations for drawing.
    canvas_size: canvas wide and heigth for drawing.ArithmeticError
    
    The image is saved in 'sierpinski.png'
    
    """
    #
    # Initialization
    #

    # Canvas
    w, h = canvas_size, canvas_size
    img  = Image.new("RGB", (w, h), color = "White")
    img1 = ImageDraw.Draw(img)

    vertices = [Point(0,h), Point(w,h), Point(w/2,0)]
    colors   = [(255,0,0), (0,255,0), (0,0,255)]

    point = Point(w/2,h/2) # initial seed

    #
    # Drawing
    #
    for i in range(n):
        r = random.randrange(0,3,1)
        vertice = vertices[r]
        color   = colors[r]
        point = (point + vertice) / 2
        img1.point((point.x,point.y), fill =color)
    img.save("sierpinski.png","PNG")

if __name__ == "__main__":
    print("Drawing Sierpinski triangle",end='')
    sierpinski()
    print(", done.")