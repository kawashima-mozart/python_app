from tkinter import *

win = Tk()

cv = Canvas(win, width =380 , height = 380)
cv.pack()

#基盤を描画
for i in range(19):
    #横の線
    y = i *20
    cv.create_line(0, y, 380, y, fill="black", width=2)
    #縦の線
    x =i * 20
    cv.create_line(x, 0, x, 380, fill="black", width = 2)

#メインループ
win.mainloop()
