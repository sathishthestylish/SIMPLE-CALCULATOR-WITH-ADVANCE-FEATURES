import math

def calculator():
    print("Welcome to the Simple Calculator with Advanced Features!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Quit")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", num1 + num2)
            elif choice == '2':
                print("Result:", num1 - num2)
            elif choice == '3':
                print("Result:", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print("Result:", num1 / num2)
            elif choice == '5':
                print("Result:", num1 ** num2)
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

calculator()
