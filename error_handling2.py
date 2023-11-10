def sum(num1, num2):
    try:
        return num1+num2
        # raise Exception("Raise an exception")
        # return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
        print(f'{err}')
        print("Please enter a number")


print(sum(5, '6'))
# print(sum(5, 0))
