from code import finding_motif_in_dna

if __name__ == "__main__":

    with (open("sample_dataset.txt") as fin,
          open("sample_output.txt") as fout):
        s, t = fin.readlines()
        locs = [int(loc) for loc in fout.readline().split()]

    ret = finding_motif_in_dna(s, t)

    assert locs == ret, \
    "Values not equal! Expecting {} - {} given." \
    .format(locs, ret)

    print("Test successful.")