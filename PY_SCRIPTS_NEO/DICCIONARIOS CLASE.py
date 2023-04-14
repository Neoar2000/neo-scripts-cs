thisdict = {
    "brand": "Ford",
    "model": ("Mustang", "Fiesta", "Focus"),
    "year": 1964
}
thisdict["sport"] = False
print(thisdict.keys())

for k in thisdict.keys():
    print(thisdict[k])