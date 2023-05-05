def intro_to_dictionary(s: str) -> dict:
  assert len(s) <= 10000, 'Line to long!'

  dict = {}

  for word in s.split():

    if word not in dict.keys():
      dict[word] = 1
    else:
      dict[word] += 1

  return dict

if __name__ == '__main__':

  with open('dataset.txt') as f:
    lines = f.readlines()

  for line in lines:
    for key, value in intro_to_dictionary(line).items():
      print(key, value)
