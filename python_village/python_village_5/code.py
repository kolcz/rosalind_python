def reading_and_writing(lines: list) -> None:
  assert len(lines) <= 1000, 'File too long!'

  with open('output.txt', 'w') as fw:

    for line in lines[1::2]:

      fw.write(line)

if __name__ == '__main__':
  with open('dataset.txt') as f:
    lines = f.readlines()

  reading_and_writing(lines)
