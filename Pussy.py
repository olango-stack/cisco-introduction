class Footballer():
    def __init__(self, name, age):
        self.name = name
        self.age = age
best = Footballer("Messi", 37)
print(best)
list_of_dictionaries = {
    0: {
        "name": "Vybz",
        "country": "Jamaica",
        "genre": "dancehall",
    },
    1: {
        "name": "Eminem",
        "country": "USA",
        "genre": "Rap",
    },
    2: {
        "name": "Ferre",
        "country": "DRC",
        "genre": "Rhumba",
    },
}
print(list_of_dictionaries[2]["name"])
index_number = 0
for x, y in list_of_dictionaries.items():
    if y == "Rhumba":
        print(index_number)
    else:
        index_number += 1    