# if, elif, else (Control structures in python)

name = input("What is your name? ")
if name =="Jessica":
    print("Hello, nice to see you {}".format(name))
elif name == "Danielle":
    print("Hello youre exacly Danielle")
elif name != "Mariah":
    print("youre not mariah")
elif name == "Kingston":
    print("Hello {}, lets have a lucn soon".format(name))

print("Have a nice day " + name)

## Conditional in Calculator

class comp_operators_functions:
    def add():
        print("This is the ADD Function")
        a = float(input("Enter a number. "))
        b = float(input("Enter another number. "))
        print(a + b)

    def substraction():
        print("This is the SUBSTRACTION Function")
        a = float(input("Enter a number. "))
        b = float(input("Enter another number. "))
        print(a - b)

    def divide():
        print("This is the DIVIDE Function")
        a = float(input("Enter a number. "))
        b = float(input("Enter another number. "))
        print(a/b)

    def multiply():
        print("This is the MULTIPLY Function")
        a = float(input("Enter a number."))
        b = float(input("Enter another number. "))
        print(a * b)

class comp_run_operators_functions:
    def run_functions():
        operation = input("Please type +, -, *, or /, to begin using the functions, and q for quit ")
        ##CONDITIONAL BLOCK
        if operation == '+':
            comp_operators_functions.add() 
        elif operation == "-":
            comp_operators_functions.substraction()
        elif operation == "/":
            comp_operators_functions.divide()
        elif operation == "*":
            comp_operators_functions.multiply()
        else:
        ##CONDITIONAL BLOCK
        ##ORDER#
            print("That operation is not available at the moment")
        ##ORDER#