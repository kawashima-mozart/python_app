from random import randint

#走行コースのデータを一行作成
def create_map_line(ginfo):
  #道路のカーブ方向を変えるか
  if randint(0,99) < 10:
    ginfo["dir"] = randint(-1,1)
  #道路の画面が端まで来たら逆向きにする
  cx, sz, gdir = (ginfo["cx"],ginfo["size"],ginfo["dir"])
  if(gdir == -1 and cx <= 1):
    ginfo["dir"] *= -1
  if (gdir == 1 and (cx + sz) >= (ginfo["cols"] - 1)):
    ginfo["dir"] *= -1
  #カーブ方向に応じて道の左端を移動
  ginfo["cx"] += ginfo["dir"]
  #道路を障害物で埋める
  line = [1] * ginfo["cols"]
  #道路部分を指定
  for i in range(ginfo["size"]):
    line[i + ginfo["cx"]] = 0
  return line

#走行コースを連続で作成
def create_map(ginfo):
  map_data = []
  for i in range(ginfo["rows"]):
    line = create_map_line(ginfo)
    map_data.insert(0,line)
  return map_data

if __name__ == "__main__":
  ginfo = {
    "rows": 20,
    "cols": 30,
    "dir": 0,
    "cx": 10,
    "size": 8
  }
  map_data = create_map(ginfo)
  for row in map_data: print(row)
