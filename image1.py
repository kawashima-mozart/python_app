from tkinter import *
from PIL import ImageTk, Image

#ウィンドウとキャンパス作成
win = Tk()
cv = Canvas(win, width=600, height=450)
cv.pack()

#画像ファイルを読み込む
filename = "photo.jpg"
img = Image.open(filename)
print("size={0}x{1}".format(img.width, img.height))

#Tkinterを使えるように変換
img_tk = ImageTk.PhotoImage(img)

#画像を表示
cv.create_image(0, 0, image=img_tk, anchor=NW)

#メインループ
win.mainloop()
