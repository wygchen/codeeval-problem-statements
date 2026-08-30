with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        lists = line.split(sep=";")
        list_a = lists[0]
        list_b = lists[1]
        list_a = set([int(i) for i in list_a.split(sep=",")])
        list_b = set([int(i) for i in list_b.split(sep=",")])
        intersection = list_a & list_b
        if intersection == set():
            print()
        else:
            print(",".join([str(i) for i in intersection]))