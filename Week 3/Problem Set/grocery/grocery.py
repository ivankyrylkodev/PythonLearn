groc = {}
while True:
    try:
        item = input().strip().upper()
        if item in groc:
            groc[item] += 1
        else:
            groc[item] = 1
    except EOFError:
        for i in sorted(groc):
            print(f"{groc[i]} {i}")
        break