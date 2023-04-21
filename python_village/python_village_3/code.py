def string_and_lists(s: str, *args) -> str:
  assert len(s) <= 200, 'String too long!'

  ret = ''
  even_it = args[::2]
  odd_it = args[1::2]

  for start_it, end_it in zip(even_it, odd_it):
    ret += s[start_it:end_it+1]
    ret += ' '

  return ret

if __name__ == '__main__':
  with open('dataset.txt') as f:
    lines = f.readlines()

  s = lines[0].rstrip('\n')
  a, b, c, d = [int(i) for i in lines[1].split()]
  ret = string_and_lists(s, a, b, c, d)

  print(ret)
