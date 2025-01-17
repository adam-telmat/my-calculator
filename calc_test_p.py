#Functions
def add(a, b):
    return a + b

def substract(a, b):
    return a- b

def multiply(a, b):
    return a * b

def devide(a, b):
    return a / b

#Different choices
print("choose operation")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Devide")

while True:
    # take input from the user
    operation = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if operation in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if operation == '1':
            print(num1, "+", num2, "=", add(num1,num2))

        elif operation == '2':
            print(num1, "-", num2, "=", substract(num1,num2))

        elif operation == '3':   
            print(num1, "*", num2, "=", multiply(num1,num2))

        elif operation == '4':
            if num2==0:
                print("Can't devide by zero")
                continue
            print(num1, "/", num2, "=", devide(num1,num2))

        #check if user wants another calculation
        next_calculation = input("let's go to next calculation ? [yes/no]")
        if next_calculation == "no":
          break
        
        #If it's not Y or N
    else:
        print("Invalid Input")
        #end