from code import consensus_and_profile, parse_fasta

if __name__ == "__main__":
    with(open("sample_dataset.txt") as fin,
         open("sample_output.txt") as fout):
        dna_matrix = parse_fasta(fin.readlines())
        profile = []
        for line in fout.readlines():
            profile.append(line.strip())
        
        ret = consensus_and_profile(dna_matrix)

        assert profile == ret, \
"Value not equal! Expecting {} - {} given." \
.format(profile, ret)

        print("Test successful.")
