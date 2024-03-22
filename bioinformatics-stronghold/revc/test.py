from code import secondary_and_tertiary_structures_dna

if __name__ == '__main__':
  with (open('sample_dataset.txt') as fin,
        open('sample_output.txt') as fout):

    lines_in = fin.readlines()
    lines_out = fout.readlines()

  sin = ''
  sout = ''

  for lin, lout in zip(lines_in, lines_out):

    sin += lin.strip('\n')
    sout += lout.strip('\n')

  assert secondary_and_tertiary_structures_dna(sin) == sout, 'Line values not equal!'

  print('Test successful.')
