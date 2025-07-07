def calculator():
    while True:
        operation = input("Enter the operation you want to perform (+, -, *, /, sqr, sqrt, exp, avg) or any other key to Exit: ").replace(" ", "").lower()
        if operation not in ["+", "-", "*", "/", "sqr", "sqrt", "exp", "avg"]:
            print("Exiting calculator. Thank you!")
            break
        if operation == "avg":
            def avg(numbers):
                total = 0
                for i in numbers:
                    total += i
                return f"The average of {numbers} is: {total / len(numbers)}"
            try:
                numbers = list(map(float, input("Enter numbers separated by space: ").split()))
                if not numbers:
                    print("No numbers entered.")
                else:
                    print(avg(numbers))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            try:
                num1 = float(input("Enter first Number: "))
                if operation == "sqr":
                    print(f"The value of square of {num1} is: {num1 ** 2}")
                elif operation == "sqrt":
                    print(f"The value of square root of {num1} is: {num1 ** 0.5}")
                else:
                    num2 = float(input("Enter second Number: "))
                    if operation == "+":
                        print(f"The value of {num1} + {num2} is: {num1 + num2}")
                    elif operation == "-":
                        print(f"The value of {num1} - {num2} is: {num1 - num2}")
                    elif operation == "*":
                        print(f"The value of {num1} * {num2} is: {num1 * num2}")
                    elif operation == "/":
                        if num2 != 0:
                            print(f"The value of {num1} / {num2} is: {num1 / num2}")
                        else:
                            print("Error: Division by 0 is not allowed.")
                    elif operation == "exp":
                        print(f"The value of {num1} ^ {num2} is: {num1 ** num2}")
            except ValueError:
                print("Invalid input! Please enter numeric values only.")
if __name__ == "__main__":
    calculator()
