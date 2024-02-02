def finding_motif_in_dna(s: str, t: str) -> tuple[int]:
    
    assert len(s) <= 1000 and len(t) <= 1000, 'String too long!'

    ret = [str(i+1) for i in range(0, len(s)-len(t)+1) if s[i:i+len(t)] == t]

    return ret

if __name__ == "__main__":

    with open("dataset.txt") as fin:
        s, t = fin.readlines()

    locs = finding_motif_in_dna(s.strip(), t.strip())

    ret = " ".join(locs)
    
    with open("output.txt", "w") as fout:
        fout.write(ret)