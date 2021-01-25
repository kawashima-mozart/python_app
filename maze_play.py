from maze_show import *
from maze_show2 import load_map_from_tsv
from PIL import Image, ImageTk
import tkinter.messagebox as msgbox

#グローバル変数の初期化
px, py = (2,2)
player_image = "player.png"

def main():
  global map_data
  #迷路データを読み込む
  map_data = load_map_from_tsv("maze2.tsv")
  #ウィンドウを作成
  create_window(map_data, [load_image,set_event])

#プレイヤーの画像を読み込む
def load_image(cv,map_data):
  global canvas, img_tk
  canvas = cv
  img = Image.open(player_image)
  img_tk = ImageTk.PhotoImage(img)
  draw_player(canvas)

#プレイヤーを描画
def draw_player(cv):
  x = px * tile_size
  y = py * tile_size
  cv.create_image(x,y,image = img_tk, anchor = NW)

#マウスイベントを登録
def set_event(cv,maze_data):
  cv.bind("<1>",canvas_click)

#キャンバスをクリックしたときの処理
def canvas_click(e):
  global px, py
  #マウス座標を得る
  mx = e.x
  my = e.y
  #移動前に前回に値を覚えておく
  px_tmp = px
  py_tmp = py
  #プレイヤーが上下左右のどこに動くかを判定
  #プレイヤーの位置を計算
  xx,yy = [px * tile_size,py * tile_size]
  ix, iy = [mx - xx, my - yy]
  if ( 0 <= ix < tile_size) and (0 <= iy < tile_size):
    pass
  elif abs(ix) > abs(iy):
    if ix > 0: px += 1
    else: px -= 1
  else:
    if iy > 0: py += 1
    else: py -= 1

  #移動先がマップデータ外ならば戻す
  if px < 0 or px >= len(map_data[0]): px = px_tmp
  if py < 0 or py >= len(map_data): px = py_tmp
  #移動先が壁ならもとに戻す
  mv = map_data[py][px]
  if mv == 1:
    px = px_tmp
    py = py_tmp
    msgbox.showinfo(message = "壁にぶつかった")
    return
  #プレイヤーを描画する
  canvas.delete("all")
  draw_map(canvas,map_data)
  draw_player (canvas)
  print("player = {0},{1}".format(px,py))
  #ゴールに辿り着いたか
  if mv == 3:
    msgbox.showinfo(message = "祝・ゴール")

if __name__ == "__main__": main()

