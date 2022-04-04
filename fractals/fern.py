import random
from PIL import Image, ImageDraw
# prueba

def fern(n=100_000,canvas_size=1000):
    """Barnsley's fern fractal ifs
    
    n: number of iterations.
    canvas_size: heigth of canvas.
    """

    # Canvas
    canvas_h = 1000
    canvas_w = 1000*6//11
    scale_factor = canvas_h//11
    x, y = 0.0, 0.0
    green = (0,255,0)
    x_offset =  2.7
    y_offset = 11.0
    
    img  = Image.new("RGB", (canvas_w, canvas_h), color = "White")
    img1 = ImageDraw.Draw(img)

    # Fern fractal calculation
    for i in range(n):
        r = random.random()
        if r < 0.01:
            xf =  0.0
            yf =  0.16*y
        elif r >= 0.01 and r < 0.86:
            xf =  0.85*x + 0.04*y
            yf = -0.04*x + 0.85*y + 1.60
        elif  r >- 0.86 and r < 0.93:
            xf =  0.20*x - 0.26*y
            yf =  0.23*x + 0.22*y + 1.60
        else:
            xf = -0.15*x + 0.28*y
            yf =  0.26*x + 0.25*y + 0.44
        x = xf
        y = yf
        
        # Drawing
        point_x = (x+x_offset)*scale_factor
        point_y = (y_offset-y)*scale_factor
        img1.point((point_x,point_y), fill = green)
    img.save("fern.png","PNG")


if __name__ == "__main__":
    print("Drawing fern fractal",end='')
    fern()
    print(", done.")
