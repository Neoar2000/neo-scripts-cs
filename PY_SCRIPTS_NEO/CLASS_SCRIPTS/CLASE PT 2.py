for i in range(2, 10):
    for j in range(1, i+1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()