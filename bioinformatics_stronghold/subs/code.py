def finding_motif_in_dna(s: str, t: str) -> tuple[int]:
    
    assert len(s) <= 1000 and len(t) <= 1000, 'String too long!'

    

    return (0,)

if __name__ == "__main__":

    with open("dataset.txt") as fin:
        s, t = fin.readlines()

    locs = finding_motif_in_dna(s)

    ret = " ".join(locs)
    with open("output.txt", "w") as fout:
        fout.write(ret)