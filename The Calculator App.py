def add(a, b):
    return a + b


print(add(2, 5))

def subtract(a, b):
    return a - b

print(subtract(9, 3))


def multiply(a, b):
    return a * b


print(multiply(3, 3))


def division(a, b):
    return a / b

print(division(14, 2))


def exponent(a, b):
    return a ** b


print(exponent(2, 3))


def modulus(a, b):
    return a % b


print(modulus(10, 2))


def user_inputs():
    print("Arithmetic operations are: ")
    print("+,-,*,/")
    user_operation = input("What arithmetic operation should I use? ")
    number_1 = int(input("What is number one? "))
    number_2 = int(input("What is number two? "))
    if user_operation == '+':
        print(add(number_1, number_2))
    elif user_operation == '-':
        print(subtract(number_1, number_2))
    elif user_operation == '*':
        print(multiply(number_1, number_2))
    elif user_operation == '/':
        print(division(number_1, number_2))
    else:
        print('Operations not Allowed!')

user_inputs()