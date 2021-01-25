from tkinter import *
from maze_show import create_window

tile_size = 20

#迷路データを取り込む
def load_map_from_tsv(filename):
  #ファイルを開く
  fp = open(filename, "rt", encoding = "utf-8")
  tsv = fp.read()
  #CSVファイルを解析
  rows = tsv.split("\n")
  result = []
  for line in rows:
    cols = line.split("\t")
    if len(cols) <= 1: break
    cols = list(map(int,cols))
    result.append(cols)
  return result

if __name__ == "__main__":
  map_data = load_map_from_tsv("maze2.tsv")
  create_window(map_data)