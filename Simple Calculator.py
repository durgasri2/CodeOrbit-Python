# Simple Calculator
# This program performs basic arithmetic operations.

try:
    # Take input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display the operations
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    # Perform the selected operation
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid choice.")

except ValueError:
    print("Error: Please enter valid numbers.")