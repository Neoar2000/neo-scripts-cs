listA = [1.5, 2.5, 3.5, 4.5, 0]
listB = [1, 2, 3, 4, 5]
listB = listB + listA

print(listB)
listB.sort()
print(listB)
listB.sort(reverse=True)
print(listB)