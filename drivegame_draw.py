from tkinter import *
from PIL import Image, ImageTk
from drivegame_info import ginfo
from drivegame_map import *

#ウィンドウとキャンバスを悪性
def create_window(ginfo):
    #ウィンドウを計算
    w = ginfo["cols"] * ginfo["tile_size"]
    h = ginfo["rows"] * ginfo["tile_size"]

    #ウィンドウとキャンバスを作成
    win = Tk()
    ginfo["cv"] = Canvas(win, width=w, height=h)
    ginfo["cv"].pack()
    #画像を読み込み
    img = Image.open("player.png")
    ginfo["car_img"] = ImageTk.PhotoImage(img)
    #走行データを作成
    ginfo["map_data"] = create_map(ginfo)
    return win

#道路と車を描画
def draw_map(ginfo):
    cv = ginfo["cv"]
    cv.delete("all")
    #道路を描画
    tile_size = ginfo["tile_size"]
    colors = ["white", "#442233"]
    for y in range(ginfo["rows"]):
        y1 = y * tile_size
        y2 = y1 + tile_size
        for x in range(ginfo["cols"]):
            x1 = x * tile_size
            x2 = x1 + tile_size
            #任意の色にタイルを描画
            v = ginfo["map_data"][y][x]
            color = colors[v]
            cv.create_rectangle(x1, y1, x2, y2,
            width=0, fill=color)
    #車を描画
    x = ginfo["car"] * ginfo["tile_size"]
    y = (ginfo["rows"] - 2) * ginfo["tile_size"]
    cv.create_image(x, y, image=ginfo["car_img"], anchor=NW)

if __name__ == "__main__":
    win = create_window(ginfo)
    draw_map(ginfo)
    win.mainloop()


