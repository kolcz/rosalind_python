def rabbits_recurrence_relations(n: int, k: int) -> int:
  assert 0 < n <= 40 and 0 < k <= 5, "Input values not within proper range!"

  fib_seq = [0]

  for i in range(1, n+1):

    match i:
      case 1:
        elem = 1
      case 2:
        elem = 1
      case _:
        elem = fib_seq[i-1]+k*fib_seq[i-2]

    fib_seq.append(elem)

  return fib_seq[n]

if __name__ == "__main__":
  with (open("dataset.txt") as fin,
       open("output.txt", "w") as fout):
    lines_in = fin.readlines()

    for line in lines_in:
      n, k = [int(i) for i in line.strip('\n').split(" ")]
      try:
        fout.write(str(rabbits_recurrence_relations(n, k))+"\n")
      except AssertionError as err:
        print(err)
        fout.write("0\n")
