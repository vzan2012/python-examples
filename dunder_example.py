class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.mydict = {
            "name": "s1",
            "has_pets": True
        }

    # Important Note: Not to modify default dunder methods
    def __str__(self):
        return f"{self.color} and {self.age}"

    def __len__(self):
        return 60

    def __call__(self):
        return "Example using __call__"

    def __getitem__(self, i):
        return self.mydict[i]


cartoon_char = Toy("blue", 10)

print(dir(cartoon_char))
print("---")
print(cartoon_char.__str__())
print(str(cartoon_char))
print("---")
print(cartoon_char.__sizeof__())
print(cartoon_char.__len__())
# print(cartoon_char.__call__())
# print(cartoon_char())
print(cartoon_char["has_pets"])
print("---")
