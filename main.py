operation = input("Enter the operation you want to perform (+, -, *, /, sqr, sqrt, exp, avg) or any other key to Exit: ").replace(" " , "").lower()
while operation:
    if operation not in ["+", "-", "*", "/", "sqr", "sqrt", "exp", "avg"]:
        print("Exiting calculator. Thankyou!")
        break
    elif operation == "avg": 
        def avg(numbers):
            sum = 0
            for i in numbers:
                sum += i
            return (f"The average of {numbers} is: {sum/len(numbers)}")
        numbers = list(map(float, input("Enter numbers seperated by space: ").split()))
        print(avg(numbers))
    else:
        num1 = float(input("Enter first Number : "))
        if operation == "sqr":
            print(f"The value of square of {num1} is: {num1**2}")
        elif operation == "sqrt":
            print(f"The value of square root of {num1} is: {num1**0.5}")
        else:
            num2 = float(input("Enter second Number : "))
        if operation == "+":
            print(f"The value of {num1} + {num2} is: {num1 + num2}")
        elif operation == "-":
            print(f"The value of {num1} - {num2} is: {num1 - num2}")
        elif operation == "*":
            print(f"The value of {num1} * {num2} is: {num1 * num2}")
        elif operation == "/":
            if num2:
                print(f"The value of {num1} / {num2} is: {num1 / num2}")
            else: print("Error: Division by 0 is not allowed.")
        elif operation == "exp":
            print(f"The value of {num1} ^ {num2} is: {num1 ** num2}")
    operation = input("Enter the operation you want to perform (+, -, *, /, sqr, sqrt, exp, avg) or any other key to cancel: ").replace(" " , "").lower()
