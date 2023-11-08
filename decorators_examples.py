# Decorators Examples

# Example 1
# def hello(func):
#     func()


# def greet():
#     print("Greetings !!!")

# print(hello(greet))


# Example 2
# def decorator(func):
#     pass


# @decorator
# def hello2():
#     pass


# decorator(hello2)

# Higher Order Functions (HOC)
# Example 3
# def greet(func):
#     return func()


# def greet2():
#     def func():
#         return 369
#     return func()

# print(greet(greet2))

# Example 3.1
# def my_decorator(func):
#     def wrap_function():
#         print('******')
#         func()
#         print('******')
#     return wrap_function
# def my_decorator(func):
#     def wrap_function(x):
#         print('******')
#         func(x)
#         print('******')
#     return wrap_function
def my_decorator(func):
    def wrap_function(*args, **kargs):
        print('******')
        func(*args, **kargs)
        print('******')
    return wrap_function
# @my_decorator
# def hello():
#     print("Welcome Hello")


@my_decorator
def hello(greeting, greeting2="optional"):
    print(f"Welcome Hello {greeting} {greeting2}")


hello('hi', 100)
# hello2 = my_decorator(hello)
# hello2()
