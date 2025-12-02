import os
from dotenv import load_dotenv
from aocd.models import Puzzle

load_dotenv()

def load_input(year: int, day: int):
  puzzle = Puzzle(year, day)
  return puzzle.input_data

def parse(input: str):
  output = input.splitlines()
  return output
