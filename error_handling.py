# Examples of Error Handling
while True:
    try:
        age = int(input("Enter your age: "))
        print(age)
    except:
        print("Enter valid number")
    else:
        print("End of the Questions")
        break
