n = int(input("Ingrese n: "))

for i in range (n):
    for j in range (1, n + 1 - i):
        print(j, end = "\t")
    print()