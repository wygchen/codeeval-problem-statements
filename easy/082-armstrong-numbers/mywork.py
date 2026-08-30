with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        n = len(line)
        number = [int(i)**n for i in line]
        number_sum = sum(number)
        print(number_sum==int(line))