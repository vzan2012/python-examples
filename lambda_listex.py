''' Examples of Lambda and List Expressions '''

my_list = [1, 2, 3, 4, 5, 6]

print(list(map(lambda item: item*2, my_list)))


# Exercise
# Square numbers
numbers = [5, 4, 3]

print(list(map(lambda item: item**2, numbers)))

# List Sorting
a = [(9, 9), (10, -1), (0, 2), (4, 3)]
a.sort(key=lambda x: x[1])

print(a)


# List Comprehensions
print([n for n in range(0, 100)])
print([n*2 for n in range(0, 100)])
print([n**2 for n in range(0, 100) if n % 2 == 0])
print([c for c in 'hello'])

# Set Comprehensions
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict = {
    key: value*2
    for key, value in simple_dict.items()
}


print(simple_dict)
print(my_dict)


my_dict2 = {
    value: value**2
    for value in [1, 2, 3]
}

print(my_dict2)


# Exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(
    set([value for value in some_list if some_list.count(value) > 1]))

print(duplicates)
