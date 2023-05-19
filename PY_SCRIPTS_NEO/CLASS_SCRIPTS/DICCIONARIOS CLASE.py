thisdict = {
    "brand": "Ford",
    "model": ("Mustang", "Fiesta", "Focus"),
    "year": 1964
}
thisdict["sport"] = False
thisdict.update({"year": 2020})
thisdict.pop("sport")
print(thisdict.values())

for k in thisdict.keys():
    print(thisdict[k])

for v in thisdict.keys():
    print(v)
for k, v in thisdict.items():
    print("llave->", k, "valor->", v)

thisdict.clear()
print(thisdict)