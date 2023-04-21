import numpy as np

def conditions_and_loops(a: int, b: int) -> int:
  assert 0 < a < b < 10000, 'Enter integers from range (0, 10000)!'

  ret = range(a+(1-a%2),b+1,2)
  return np.sum(ret)

if __name__ == '__main__':

  with open('dataset.txt') as f:
    lines = f.readlines()

  for line in lines:
    a, b = [int(i) for i in line.split()]
    print(conditions_and_loops(a, b))
