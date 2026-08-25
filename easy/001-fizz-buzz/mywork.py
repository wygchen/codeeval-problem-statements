with open('input.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        X = int(numbers[0])
        Y = int(numbers[1])
        N = int(numbers[2])

        for i in range(1, N+1):
            text = ""
            if i%X==0:
                text += "F"
            if i%Y==0:
                text += "B"
            if text=="":
                text = str(i)
            print(text, end=" ")

        print()            