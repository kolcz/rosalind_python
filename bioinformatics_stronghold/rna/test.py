from code import second_nucleic_acid

if __name__ == '__main__':

  with open('sample_dataset.txt') as in_f, \
      open('sample_output.txt') as out_f:
    in_lines = in_f.readlines()
    out_lines = out_f.readlines()

  in_line = ''
  out_line = ''

  for line in in_lines:
    in_line += line.strip('\n')

  for line in out_lines:
    out_line += line.strip('\n')

  assert second_nucleic_acid(in_line) == out_line, 'Line values not equal!'

  print('Test successful.')

