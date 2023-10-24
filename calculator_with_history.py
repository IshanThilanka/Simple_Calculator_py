# Initialize a list to store previous operations
previous_operations = []

def add(a, b):
    result = a + b
    previous_operations.append(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    previous_operations.append(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    previous_operations.append(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print(e)
        result = None  # Set result to None in case of an exception
    
    previous_operations.append(f"{a} / {b} = {result}")
    return result

def power(a, b):
    result = a ** b
    previous_operations.append(f"{a} ^ {b} = {result}")
    return result

def remainder(a, b):
    result = a % b
    previous_operations.append(f"{a} % {b} = {result}")
    return result

def select_op(choice):
    if choice == "#":
        return -1
    elif choice == "$":
        return 0
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1
            try:
                num1 = float(num1s)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue

        while True:
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue

        result = 0.0
        last_calculation = ""
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something Went Wrong")

        last_calculation = f"{num1} {choice} {num2} = {result:}"
        print(last_calculation)
    elif choice == "?":
        history()  # Call the history() function to display previous operations
    else:
        print("Unrecognized operation")

def history():
    if not previous_operations:
        print("No past calculations to show")
    else:
        
        for operation in previous_operations:
            print(operation)

while True:
    print("Select operation.")
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $")
    print("8.History  : ?")

    # Take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice) == -1:
        # Program ends here
        print("Done. Terminating")
        break
