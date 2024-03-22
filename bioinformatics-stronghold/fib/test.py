from code import rabbits_recurrence_relations

if __name__ == "__main__":
  with (open("sample_dataset.txt") as fin,
        open("sample_output.txt") as fout):

    lines_in = fin.readlines()
    lines_out = fout.readlines()

  for lin, lout in zip(lines_in, lines_out):

    sin = [int(i) for i in lin.strip("\n").split(" ")]
    sout = int(lout.strip("\n"))

    try:
      assert rabbits_recurrence_relations(*sin) == sout, "Line values not equal!"
    except TypeError:
      print("Too many input arguments!")
      raise
    else:
      print("Test Successful.")
