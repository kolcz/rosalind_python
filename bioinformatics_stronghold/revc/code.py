def secondary_and_tertiary_structures_dna(s: str = '') -> str:

  assert 0 < len(s) <= 1000, 'Non compatible input string!'

  rev_compl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

  sc = ''

  for c in s[::-1]:
    sc += rev_compl[c]

  return sc

if __name__ == '__main__':

  with open('dataset.txt') as fin:
    lines_in = fin.readlines()

  s = ''

  for line in lines_in:
    s += line.strip('\n')

  with open('output.txt', 'w') as fout:
    fout.write(secondary_and_tertiary_structures_dna(s))
