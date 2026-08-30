with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        x, n = map(int, line.split(','))

        # time O(1)
        # space O(1)
        result = (x+n-1) & ~(n-1)
        print(result)

# clearing bits (~(n-1)): multiple of 8 always end in three zeros, to round any binary numbr down to a multiple of 8, we just clear the last 3 bits t be zero
