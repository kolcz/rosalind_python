import numpy as np

def consensus_and_profile(dna_matrix: np.ndarray) -> list[str]:
    l = dna_matrix.shape[1]
    a = np.zeros(l, dtype=np.str_)
    c = np.zeros(l, dtype=np.str_)
    g = np.zeros(l, dtype=np.str_)
    t = np.zeros(l, dtype=np.str_)
    consensus = ""

    for i in range(l):
        a[i] = str(len(np.where(dna_matrix[:, i] == "A")[0]))
        c[i] = str(len(np.where(dna_matrix[:, i] == "C")[0]))
        g[i] = str(len(np.where(dna_matrix[:, i] == "G")[0]))
        t[i] = str(len(np.where(dna_matrix[:, i] == "T")[0]))
        
        m = max(a[i], c[i], g[i], t[i])
        if m == a[i]:
            consensus += "A"
        elif m == c[i]:
            consensus += "C"
        elif m == g[i]:
            consensus += "G"
        elif m == t[i]:
            consensus += "T"

    ret = []
    ret.append(consensus)
    ret.append(" ".join(("A:", *a)))
    ret.append(" ".join(("C:", *c)))
    ret.append(" ".join(("G:", *g)))
    ret.append(" ".join(("T:", *t)))
    
    return ret

def parse_fasta(lines: list[str]) -> np.ndarray:
    row = ""
    for line in lines[1:]:
        if line.startswith(">"):
            break
        else:
            row += line.strip()

    str_len = len(row)
    str_num  = len(tuple(filter(lambda l: l.startswith(">"), lines)))
    assert str_len <= 1000, "DNA string is too long"
    assert str_num <= 10, "Too many DNA strings"
    
    dna_matrix = np.empty((0, str_len), dtype=np.str_)
    row = ""

    for line in lines:
        if line.startswith(">"):
            if len(row) > 0:
                dna_matrix = np.concat((dna_matrix, [[*row]]))
            row = ""
        else:
            row += line.strip()

    dna_matrix = np.concat((dna_matrix, [[*row]]))

    return dna_matrix

if __name__ == "__main__":
    with open("dataset.txt") as fin:
        dna_matrix = parse_fasta(fin.readlines())

    ret = consensus_and_profile(dna_matrix)

    with open("output.txt", "w") as fout:
        for line in ret:
            fout.write(line + "\n")