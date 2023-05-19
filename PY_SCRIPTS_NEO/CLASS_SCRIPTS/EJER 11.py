num = int(input("Introduce un número: "))
fact = 1

while num > 0:
    fact *= num
    num -= 1

print(fact)