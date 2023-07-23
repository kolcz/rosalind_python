import io
import re
import numpy as np

def parse_FASTA(dataset_fasta: io.TextIOWrapper) -> dict:

  dna_strings = {}

  lines = dataset_fasta.read()

  mtchs = re.findall(">[^>]+",lines)

  assert len(mtchs) <= 10, "Too many DNA strings!"

  for mtch in mtchs:
    mtch_spl = mtch.lstrip(">").split("\n")
    dna_strings[mtch_spl[0]] = "".join(mtch_spl[1:])

  return dna_strings


def computing_gc_content(dna_str: str) -> float:

  dna_arr = np.array([s for s in dna_str])

  s_len = len(dna_arr)

  assert s_len <= 1000, "DNA string too long!"

  g_len = len(*np.where(dna_arr == "G"))
  c_len = len(*np.where(dna_arr == "C"))

  return ((g_len + c_len)/s_len)*100

if __name__ == "__main__":
  with open("dataset.txt") as fin:
    dna_strings = parse_FASTA(fin)

  gc_val = 0

  for dna_id, dna_str in dna_strings.items():
    cont = computing_gc_content(dna_str)
    if cont > gc_val:
      gc_val = cont
      id_val = dna_id

  with open("output.txt", "w") as fout:
    fout.write(id_val+"\n"+str(gc_val))
