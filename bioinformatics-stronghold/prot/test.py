from code import translating_rna_into_protein

if __name__ == "__main__":

    with (open("sample_dataset.txt") as fin,
          open("sample_output.txt") as fout):
        s = fin.read()
        enc_s = fout.read()

    ret = translating_rna_into_protein(s)

    assert enc_s == ret, \
    "Values not equal! Expecting {} - {} given." \
    .format(enc_s, ret)

    print("Test successful.")