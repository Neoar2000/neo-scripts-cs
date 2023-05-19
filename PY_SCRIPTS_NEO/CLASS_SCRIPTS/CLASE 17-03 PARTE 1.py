num = 0
menor = 100
for i in range(10):
    print(num, menor, i)
    num = int(input("Introduzca un numero: "))
    if num % menor:
        menor = num

print(menor)