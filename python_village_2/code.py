def square_hypotenuse_right_triangle(a: int, b: int) -> int:
  assert (a < 1000 and b < 1000), 'Number greater than expected. Type numbers lower than 1000.'
  return a*a+b*b

if __name__ == '__main__':

  with open('dataset.txt') as f:
    line = f.readline()

  nums = [int(num) for num in line.split()]

  ret = square_hypotenuse_right_triangle(nums[0], nums[1])
  print(ret)
