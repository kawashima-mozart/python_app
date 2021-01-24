from tkinter import *


def random_color():
     from random import randint
     rnd = lambda : randint(0,255)

     r = rnd()
     g = rnd()
     b = 255

     f = "#{0:02x}{1:02x}{2:02x}"
     color = f.format(r, g, b)
     return color

def draw_circles():
    cv.delete("all")
    for y in range(20):
        y1 = y * 20
        y2 = y1 + 20
        for x in range(30):
            x1 = x * 20
            x2 = x1 + 20

            color = random_color()
            cv.create_oval( x1, y1, x2, y2,
                            fill = color ,width = 0)

    win.after(100, draw_circles)
    
win = Tk()

cv = Canvas(win, width =600 , height = 400)
cv.pack()

win.after(1, draw_circles)

#メインループ
win.mainloop()
