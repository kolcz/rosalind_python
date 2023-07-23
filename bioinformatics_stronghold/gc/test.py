from code import parse_FASTA, computing_gc_content

if __name__ == "__main__":

  with (open("sample_dataset.txt") as fin,
        open("sample_output.txt") as fout):
    dna_strings = parse_FASTA(fin)
    id = fout.readline().rstrip("\n")
    gc_cont = float(fout.readline())

  gc_val = 0

  for dna_id, dna_str in dna_strings.items():
    cont = computing_gc_content(dna_str)
    if cont > gc_val:
      gc_val = cont
      id_val = dna_id

  assert id == id_val and gc_cont - gc_val < 0.001, \
         "Values not equal!\n Curr ID = {}; Curr GC Content = {}\n \
         Prop ID = {}; Prop GC Content = {}".format(id_val, gc_val, id, gc_cont)

  print("Test successful.")
