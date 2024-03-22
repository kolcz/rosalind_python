import io

def readline(f:io.TextIOWrapper) -> str:
  return f.readline().rstrip("\n")

def counting_point_mutations(s: str, t: str) -> int:

  len_s = len(s); len_t = len(t)

  assert (len_s == len_t and len_s <= 1000), \
         "DNA strings don't meet the conditions!"

  comp_arr = [1 for i,j in zip(s,t) if i != j]

  return len(comp_arr)

if __name__ == "__main__":
  with open("dataset.txt") as fin:
    s,t = [readline(fin) for i in range(2)]

  hamm_dist = counting_point_mutations(s, t)

  with open("output.txt", "w") as fout:
    fout.write(str(hamm_dist))
