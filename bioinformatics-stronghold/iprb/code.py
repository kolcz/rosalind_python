def mendels_first_law(k: int, m: int, n: int) -> float:

    assert k > 0 and m > 0 and n > 0, \
            "Input doesn't meet the condition. Expected values greater than 0!"

    s = k + m + n
    mm = (m/s)*((m-1)/(s-1))*0.25
    mn = (m/s)*(n/(s-1))*0.5
    nn = (n/s)*((n-1)/(s-1))

    return round(1 - (mm + 2*mn + nn), 5)

if __name__ == "__main__":
    with open("dataset.txt") as fin:
        k, m, n = [int(i) for i in fin.readline().rstrip().split()]

    prob = mendels_first_law(k, m, n)

    with open("output.txt", "w") as fout:
        fout.write(str(prob))
