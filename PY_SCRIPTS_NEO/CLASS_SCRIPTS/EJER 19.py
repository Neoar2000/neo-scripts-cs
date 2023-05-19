com = 0
sum = 0
x = 2

while com <= 100:
    primo = True
    for i in range(2, x // 2):
        if x % i == 0:
            primo = False
            break
    if primo == False:
        com += 1
    sum += x**2
    x = x + 1
    print(x)