from code import counting_point_mutations, readline


if __name__ == "__main__":

  with (open("sample_dataset.txt") as fin,
        open("sample_output.txt") as fout):
    s,t = [readline(fin) for i in range(2)]
    hamm_dist = int(readline(fout))

  ret = counting_point_mutations(s, t)

  assert  hamm_dist == ret, \
          "Values not equal! Expecting {} - given {}."\
          .format(hamm_dist, ret)

  print("Test successful.")
