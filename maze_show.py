from tkinter import *

tile_size = 20

#迷路データを取り込む
def load_map_data():
  from maze_data import data
  return data

#迷路を表示
def draw_map(cv,data):
  #左から右下へと描画
  rows = len(data)
  cols = len(data[0])
  for y in range(rows):
    y1 = y *tile_size
    y2 = y1 * tile_size
    for x in range(cols):
      x1 = x * tile_size
      x2 = x1 * tile_size
      #x,yから対応するデータのリスト値を取得する
      p = data[y][x]
      #値に応じた色を決定する
      if p == 0: color = "white"
      if p == 1: color = "#404040"
      if p == 2: color = "red"
      if p == 3: color = "blue"
      #正方形を表示
      cv.create_rectangle(
        x1,y1,x2,y2,
        fill = color,
        outline = "black",width = 2
      )
#ウィンドウとキャンパスを作成
def create_window(map_data, events = []):
  win = Tk()
  win.title("迷路")
  rows = len(map_data)
  cols = len(map_data[0])
  cv = Canvas(win,
          width = (cols * tile_size),
          height = (rows * tile_size))
  cv.pack()
  draw_map(cv,map_data)
  #追加処理
  for func in events: func(cv,map_data)
  win.mainloop()

if __name__ == "__main__":
  map_data = load_map_data()
  create_window(map_data)