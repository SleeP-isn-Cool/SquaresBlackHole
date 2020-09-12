import tkinter
import random
canvas = tkinter.Canvas(width=640, height=480, bg="gray")
canvas.pack()
def long(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
def colour(vzd):
    normalize = 255 - int((vzd/400)*255)
    print(vzd,normalize)
    return "#{0:02x}{0:02x}{0:02x}".format(normalize)
def create_square(x, y, size, colour):
    place = (x-size/2, y-size/2, x+size/2, y+size/2)
    canvas.create_rectangle(place, fill=colour)
def create_squares(much):
    for x in range(much):
        x = random.randrange(640)
        y = random.randrange(480)
        vzd = long(x,y,320,240)
        color = colour(vzd)
        create_square(x,y, vzd/6, color)
create_squares(1000)
canvas.mainloop()
