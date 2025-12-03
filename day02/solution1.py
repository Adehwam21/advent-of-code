import os 

def read_input(file_name: str):
  base_dir = os.path.dirname(__file__)
  file_path = os.path.join(base_dir, file_name)

  with open(file_path, "r") as f:
      data = f.read().split(",")
  return data

def answer():
  cases = read_input("input.txt")
  invalid_sum = 0
  
  for r in cases:
    interval = r.split("-")
    start = int(interval[0])
    end = int(interval[-1])

    for num in range(start, end+1):
      num_str = str(num)
      num_length = len(num_str)

      # select numbers that are of even length
      if num_length % 2 == 1:
        continue

      # check if first half of the number equals the other half
      first_half = num_str[0:(num_length // 2)]
      second_half = num_str[(num_length // 2):]

      if first_half == second_half:
        invalid_sum += num
  return invalid_sum