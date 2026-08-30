with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        digits = [int(i) for i in list(line)]
        print(sum(digits))

    