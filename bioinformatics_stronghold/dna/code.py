

def counting_dna_nucleotides(s: str) -> str:

  assert len(s) <= 1000, 'Input string too long!'

  d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

  for c in s:
    if c in d.keys():
      d[c] += 1

  return '{} {} {} {}'.format(*d.values())

if __name__ == '__main__':

  with open('dataset.txt') as f:
    lines = f.readlines()

  for line in lines:
    print(counting_dna_nucleotides(line))
