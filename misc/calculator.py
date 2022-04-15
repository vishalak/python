def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Available operations: \n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Exit")
while True:
    selection = int(input("Please select an operation from 1, 2, 3, 4, 5: "))
    if selection == 5: 
        print("Thank you for using this app!")
        break
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if selection == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif selection == 2:
         print(num1, "-", num2, "=", subtract(num1, num2))
    elif selection == 3:
         print(num1, "*", num2, "=", multiply(num1, num2))
    elif selection == 4:
         print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

