import os
import time

def calculate_time_taken(function):
  """Calculates the time taken to run a function."""

  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()  # High-precision counter
    result = function(*args, **kwargs)
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    print(f"Function '{function.__name__}' took {time_taken:.4f} seconds to run.")
    return result

  return wrapper

def fetch(day):
    file = os.getcwd() + f"\\input_{day}.txt"
    if os.path.exists(file):
        with open(file, "r") as f:
            return f.read()
    else:
        print(f"input_{day}.txt not found.")


def run(solution):
    sol = solution()
    
    @calculate_time_taken
    def p1():
        print("Part 1: ", sol.calculate_p1())

    @calculate_time_taken
    def p2():
        print("Part 2: ", sol.calculate_p2())
    
    p1()
    p2()
