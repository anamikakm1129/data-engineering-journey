#Day 7: mini script (calculator)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    
    choice = input("Enter choice: ")

    # validate choice
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice")
        continue

    # exit condition
    if choice == '5':
        print("Exiting...")
        break

    # take input numbers
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except:
        print("Invalid input")
        continue

    # apply logic
    if choice == '1':
        result = add(a, b)
    elif choice == '2':
        result = subtract(a, b)
    elif choice == '3':
        result = multiply(a, b)
    elif choice == '4':
        result = divide(a, b)

    # print result
    print("Result:", result)