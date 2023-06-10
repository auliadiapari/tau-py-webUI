
## Loops
fruits = ["Apple", "Banana", "Grapes", "Dragon Fruit"]
for fruit in fruits:
    print("Would you like {} ?".format(fruit))


for number in range(1, 20):
    print("Numbers {}".format(number))

## While Loops
temp_f = 40

while temp_f > 32:
    print("the water is {} degrees.".format(temp_f)) #this will doing the infinte loop if ln16 is being deleted/commented
    temp_f -= 1  #this will decrease the value of temps by 1

# Loop Control (Break, Continue)
# Break
    if temp_f == 33:
        break #this condition will stop once the variable (temp_f) reach the desired value (33)

# Continue
for numbers in range(1,15):
    if numbers == 7:
        print("Were skipping number 7.")
        continue # allows us to skip certain sections of a loop but allows the loop to keep going
    print("This is the number {}.".format(numbers))

# Pass
for numbers in range (1,15):
    if numbers == 7:
        pass # Pass automatically skips over un-implemented parts of the code
    else:
        print("The number is {}. ".format(numbers))
#------------------------------------------------------------------

# While Loops in Calculators (Comparison Operators)


on = True
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

while on:
    operation = input("Please type +, -, *, or /, to begin using the functions, and q for quit ")
        
    if operation == '+':
        add() 
    elif operation == "-":
        substraction()
    elif operation == "/":
        divide()
    elif operation == "*":
        multiply()
    elif operation == "q":
        on = False
    else:
            print("That operation is not available at the moment")
        

    
        












