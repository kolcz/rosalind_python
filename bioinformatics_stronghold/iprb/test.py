from code import mendels_first_law

if __name__ == "__main__":

    with (open("sample_dataset.txt") as fin,
          open("sample_output.txt") as fout):
        k, m, n = [int(i) for i in fin.readline().rstrip().split()]
        prob = float(fout.readline().rstrip())

    ret = mendels_first_law(k, m, n)

    assert prob == ret, \
           "Values not equal! Expecting {} - given {}."\
           .format(prob, ret)

    print("Test successful.")
