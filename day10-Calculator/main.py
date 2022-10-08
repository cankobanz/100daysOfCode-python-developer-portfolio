from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What is the first number?\n"))
    for operation in operations:
        print(operation)
    operation_symbol = input("Pick an operation from the line above: \n")

    num2 = float(input("What is the next number?\n"))

    answer = operations[operation_symbol](num1, num2)

    flag = True
    while flag:
        decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: \n")
        if decision == "n":
            flag = False
            continue
        elif decision == "y":
            for operation in operations:
                print(operation)
            operation_symbol = input("Pick an operation from the line above: ")

            num2 = float(input("What is the next number?"))

            answer = operations[operation_symbol](answer, num2)
            print(f"{answer} {operation_symbol} {num2} = {answer}")

        else:
            print("Please type either 'y' or 'n'!")


calculator()
