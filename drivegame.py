from drivegame_info import ginfo
from drivegame_map import create_map_line
from drivegame_draw import *
import tkinter.messagebox as msgbox

#ゲームの初期化
def init_game():
  global win
  #ウィンドウやキャンバスの生成と走行コースも生成
  win = create_window(ginfo)
  #キーボードイベントを設定
  win.bind("<Left>",key_event_left)
  win.bind("<Right>",key_event_right)

  #ゲームを開始する
  game_loop()
  win.mainloop()

  #カーソルキーを押したときの処理
def key_event_left(e):
  if ginfo["car"] > 0:
    ginfo["car"] -= 1
  
def key_event_right(e):
  if ginfo["car"] <= ginfo["cols"] - 1:
    ginfo["car"] += 1

#ゲームループ
def game_loop():
  #走行コースと自動車の描画
  draw_map(ginfo)
  win.title("ドライブゲーム スコア=" + str(ginfo["score"]))
  #ゲームオーバ−判定
  map_data = ginfo["map_data"]
  v = map_data[ginfo["rows"] - 2][ginfo["car"]]
  if v != 0:
    msgbox.showinfo(title = "ゲームオーバー",
                message = "コースアウトしました\n"
                "sスコア=" + str(ginfo["score"]))
    quit()
  #スコアを加算
  ginfo["score"] += 10
  #過ぎた道路を消す
  del(map_data[ginfo["rows"] - 1])
  line = create_map_line(ginfo)
  map_data.insert(0,line)
  #一定時間後にこの関数を実行
  win.after(100,game_loop)

if __name__ == "__main__":init_game()



