with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        integers = [int(i) for i in line.split(sep=",")]
        uniques = set(integers)
        uniques_str = [str(i) for i in uniques]
        print(",".join(uniques_str))