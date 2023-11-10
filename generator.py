# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result


# my_list = make_list(10)
# print(my_list)


# def make_list2(num):
#     result = [i*2 for i in range(num)]
#     return result


# print(make_list2(10))


# Creating a generator function
def generator_function(n):
    for i in range(n):
        yield i*2


for item in generator_function(10):
    print(item)

g = generator_function(20)
print(next(g))
print(next(g))
print(next(g))
