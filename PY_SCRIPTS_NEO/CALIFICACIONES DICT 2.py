texto = input("Ingrese un texto: ")
caracteres = dict()

for i in texto:
    if i in caracteres:
        caracteres[i] += 1
    else:
        caracteres[i] = 1

print(caracteres)