from art import logo
# Calculator

# Add
def add(nbr1, nbr2):
    return nbr1 + nbr2

# Subtract
def subtract(nbr1, nbr2):
    return nbr1 - nbr2

# Multiply
def multiply(nbr1, nbr2):
    return nbr1 * nbr2

# Divide
def divide(nbr1, nbr2):
    return nbr1 / nbr2



operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)
    to_continue = True

    while to_continue:
        operation_symble = input("Pick an operation from the line above: ")

        num2 = float(input("What is next number?: "))
        calculation = operations[operation_symble]
        answer = calculation(num1,num2)

        print(f"{num1} {operation_symble} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit : ").lower() == "y":
            num1 = answer
        else:
            to_continue = False
            calculator()

calculator()








