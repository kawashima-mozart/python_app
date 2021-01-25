from tkinter import *
import tkinter.messagebox as msgbox

def main():
  global cv
  #ウィンドウとキャンバスを作成
  win = Tk()
  cv = Canvas(win, width=400, height = 300)
  cv.pack()
  #イベントの設定
  cv.bind("<1>", canvas_click)
  win.mainloop()

def canvas_click(e):
  global cv
  mx = e.x
  my = e.y
  #円を描画
  cv.create_oval(
    mx - 10, my - 10, mx +10, my + 10,
    fill = "red"
  )

main()
