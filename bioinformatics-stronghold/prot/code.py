import yaml

def translating_rna_into_protein(s: str) -> str:

    assert len(s) <= 10**4, \
    "Input string is too long!"

    codon_dict = yaml.safe_load(open("rna_codon_table.yaml"))
    stop_dict = yaml.safe_load(open("stop_codon_table.yaml"))

    enc_s = ""

    for i in range(0, len(s), 3):
        
        sub_s = s[i:i+3]

        if sub_s in stop_dict:
            break

        if sub_s in codon_dict:
            enc_s += codon_dict[sub_s]

    return enc_s

if __name__ == "__main__":

    with open("dataset.txt") as fin:
        s = fin.read()

    enc_s = translating_rna_into_protein(s)

    with open("output.txt", "w") as fout:
        fout.write(enc_s)