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

    #edge cases
    case1 = (currentPosition >= oldPosition and num <= 0)
    case2 = (currentPosition <= oldPosition and num >= 0)
    case3 = oldPosition != 0
    case4 = currentPosition == 0

    if ((case1 or case2 ) and case3) or case4:
      count += (abs(num) // 100) + 1
    else:
      count += (abs(num) // 100) + 0
  return count
