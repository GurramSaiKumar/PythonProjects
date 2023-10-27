while True:
    print("Choose menu: ")
    print("Enter add for addition")
    print("Enter sub for subtraction")
    print("Enter mul for multiplication")
    print("Enter div for division")
    print("Enter exit to end program")
    user_input = input("Choose from menu")
    if user_input == 'exit':
        break
    first = int(input("enter first number: "))
    second = int(input("enter second number: "))
    if user_input == 'add':
        result = first + second
        print(result)
    elif user_input == 'sub':
        result = first - second
        print(result)
    elif user_input == 'mul':
        result = first * second
        print(result)
    elif user_input == 'div':
        result = first / second
        print(result)
    else:
        print("Invalid option. Choose correct")
