''' Example of Iterator '''
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break

# special_for([1, 2, 3, 5, 5])

''' MyGen Class - Generators '''


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


for i in MyGen(0, 5):
    print(i)
