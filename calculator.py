
def calculator():
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Km to Miles")
        print("6. Celsius to Fahrenheit")
        print("7. INR to USD")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "8":
            print("Thank you!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice! Try again.")
            continue

        while True:
            try:
                number = float(input("Enter the value: "))
                break
            except ValueError:
                print("Invalid input! Enter a number.")

        if choice in ["1", "2", "3", "4"]:
            while True:
                try:
                    number2 = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input! Enter a number.")

            if choice == "1":
                print("Result:", number + number2)
            elif choice == "2":
                print("Result:", number - number2)
            elif choice == "3":
                print("Result:", number * number2)
            elif choice == "4":
                if number2 == 0:
                    print("Cannot divide by zero!")
                else:
                    print("Result:", number / number2)

        elif choice == "5":
            print("Miles:", number * 0.621371)

        elif choice == "6":
            print("Fahrenheit:", (number * 9 / 5) + 32)

        elif choice == "7":
            print("USD:", round(number / 83.33, 2))
            print("Approximate exchange rate only.")

calculator()
