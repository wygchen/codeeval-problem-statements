with open('input.txt', 'r') as file:
    for line in file:
        words = line.split()
        reversed_words = words[::-1]
        print(" ".join(reversed_words))
