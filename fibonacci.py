# Fibonacci Numbers
def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp+b


for z in fibo(5):
    print(z)


def fibo2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp+a
    return result


print(fibo2(5))
