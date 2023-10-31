''' Examples of Pure Functions '''


# Older Style

# def multiple_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiple_by2([1, 2, 3]))

# map function

my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, my_list)))


# filter function
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))


# zip function
your_list = [10, 20, 30]
their_list = [5, 4, 3, 2]
print(list(zip(my_list, your_list, their_list)))
