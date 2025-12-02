import os
import math

def read_input(file_name: str):
  base_dir = os.path.dirname(__file__)
  file_path = os.path.join(base_dir, file_name)

  with open(file_path, "r") as f:
      data = f.read()
      lines = data.splitlines()
  return lines


def answer():
  data = read_input("input.txt")
  currentPosition = 50
  count = 0
  for move in data:
    num = (-1 if move[0] == "L" else 1) * int(move[1:])
    oldPosition = currentPosition
    currentPosition = (currentPosition + num) % 100
    count += (abs(num) // 100) + (1 if (((currentPosition >= oldPosition and num <= 0) or (currentPosition <= oldPosition and num >= 0)) and oldPosition != 0) or currentPosition == 0 else 0)
  return count
