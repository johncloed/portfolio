import math

while True:
    print("Choose a math function to calculate:")
    print("1. Square root")
    print("2. Logarithm")
    print("3. Factorial")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = float(input("Enter a number: "))
        result = math.sqrt(num)
        print("The square root of", num, "is", result)
    elif choice == 2:
        num = float(input("Enter a number: "))
        base = float(input("Enter the base of the logarithm: "))
        result = math.log(num, base)
        print("The logarithm of", num, "with base", base, "is", result)
    elif choice == 3:
        num = int(input("Enter a number: "))
        result = math.factorial(num)
        print("The factorial of", num, "is", result)
    elif choice == 0:
        break
    else:
        print("Invalid choice")

    print()