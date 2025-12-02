import os

def read_input(file_name: str):
  base_dir = os.path.dirname(__file__)
  file_path = os.path.join(base_dir, file_name)

  with open(file_path, "r") as f:
      data = f.read()
      lines = data.splitlines()

  return lines

def answer():
  test_case = read_input("input2.txt")

  # Solution
  curr_position = 50
  end = 100
  zero_count = 0

  for rotation in test_case:
    direction = rotation[0]
    displacement = int(rotation[1:])
    
    if direction == "L":
      curr_position = (curr_position - displacement) % end
    elif direction == "R":
      curr_position = (curr_position + displacement) % end
    
    if curr_position == 0: 
      zero_count +=1
  
  return zero_count
