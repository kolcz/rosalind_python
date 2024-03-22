from code import finding_motif_in_dna

if __name__ == "__main__":

    with (open("sample_dataset.txt") as fin,
          open("sample_output.txt") as fout):
        s, t = fin.readlines()
        locs = [loc for loc in fout.readline().split()]

    ret = finding_motif_in_dna(s.strip(), t.strip())

    assert locs == ret, \
    "Values not equal! Expecting {} - {} given." \
    .format(locs, ret)

    print("Test successful.")