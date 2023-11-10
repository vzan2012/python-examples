# Examples of Error Handling
while True:
    try:
        age = int(input("Enter your age: "))
        print(age)
    except ValueError:
        print("Enter valid number")
        continue
    except ZeroDivisionError:
        print("Please enter age higher than zero")
        break
    else:
        print("End of the Questions")
        break
    finally:
        print("End of the program")
