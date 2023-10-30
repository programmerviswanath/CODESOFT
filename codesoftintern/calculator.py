
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Denominator should not be Zero"
    return x / y

while True:
    print("Options:")
    print("Enter 'a' for addition")
    print("Enter 'b' for subtraction")
    print("Enter 'c' for multiplication")
    print("Enter 'd' for division")
    print("Enter 'e' to end the program")
    
    choice = input("Please enter choice [a/b/c/d/e]: ")

    if choice == 'e':
        break

    if choice in ("a", "b", "c", "d"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "a":
            print("Result: ", add(num1, num2))
        elif choice == "b":
            print("Result: ", subtract(num1, num2))
        elif choice == "c":
            print("Result: ", multiply(num1, num2))
        elif choice == "d":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result: ", result)
    else:
        print("Invalid input")
