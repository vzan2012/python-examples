''' Examples of Pure Functions '''
from functools import reduce

# Older Style

# def multiple_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiple_by2([1, 2, 3]))

# map function

# my_list = [1, 2, 3]


# def multiply_by2(item):
#     return item*2


# print(list(map(multiply_by2, my_list)))


# filter function
# def only_odd(item):
#     return item % 2 != 0


# print(list(filter(only_odd, my_list)))


# zip function
# your_list = [10, 20, 30]
# their_list = [5, 4, 3, 2]
# print(list(zip(my_list, your_list, their_list)))


# reduce function
# def accumulator(acc, item):
#     return acc+item


# print(reduce(accumulator, your_list, 0))

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.upper()


print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def passOverScore(item):
    return item > 50


print(list(filter(passOverScore, scores)))


# 4 reduce - combine all numbers:
def accumulator(acc, item):
    return acc+item


print(reduce(accumulator, (scores+my_numbers), 0))
