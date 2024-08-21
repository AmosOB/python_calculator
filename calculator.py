def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

while True:
    try:
        num1 = float(input(f"Enter Number One: "))
        sign = input("Enter Sign (+, -, *, /): ")
        num2 = float(input(f"Enter Number Two: "))
    except ValueError:
        print(f"Please enter valid numbers.")
        continue
    
    if sign == '+':
        answer = add(num1, num2)
    elif sign == '-':
        answer = subtract(num1, num2)
    elif sign == '*':
        answer = multiply(num1, num2)
    elif sign == '/':
        answer = divide(num1, num2)
    else:
        print('Not that advanced yet!')
        continue
    
    print(f"The answer is: {answer}")
    break
