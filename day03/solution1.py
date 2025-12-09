import os 

def read_input(file_name: str):
  base_dir = os.path.dirname(__file__)
  file_path = os.path.join(base_dir, file_name)

  with open(file_path, "r") as f:
      data = f.read().splitlines()
  return data

def max_joltage(s: str) -> int:
  digits = list(map(int, s))
  best = -1
  max_right = -1
  for d in reversed(digits):
    if max_right != -1:  
      best = max(best, d * 10 + max_right)
    max_right = max(max_right, d)
  return best

def answer():
  cases = read_input("input.txt")
  nums = []
  for case in cases:
     num = max_joltage(case)
     nums.append(num)
  return sum(nums)
