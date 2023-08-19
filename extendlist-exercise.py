
class SuperList(list):
    def __len__(self):
        return 1000


print(dir(SuperList))

super_list1 = SuperList()

super_list1.append(10)
print(super_list1)

print(len(super_list1))

print(issubclass(SuperList, list))
