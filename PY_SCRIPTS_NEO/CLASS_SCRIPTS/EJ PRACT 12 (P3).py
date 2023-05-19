n = int(input("Ingrese n: "))

while n >= 1:
    for i in range(1, n+1):
        print(i, end="\t")
    print()

    for i in range(n, 0, -1):
        print(i, end="\t")
    print()
    
    n -= 1