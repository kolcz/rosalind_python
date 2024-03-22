import re

def second_nucleic_acid(t: str) -> str:
  assert len(t) <= 1000, 'String too long!'

  ret = re.sub('T', 'U', t)
  return ret

if __name__ == '__main__':

  with open('dataset.txt') as f:
    lines = f.readlines()

  in_str =  ''

  for line in lines:
    in_str += line.strip('\n')

  with open('output.txt', 'w') as fw:
    fw.write(second_nucleic_acid(in_str))

