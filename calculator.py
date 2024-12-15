operation = input("Enter the operator to perform ( + , - , / , * , % )= ")
if (operation == "+"or operation =="-" or operation =="/" or operation =="*" or operation =="%"):
    num1 = float(input("Enter the 1st number = "))
    num2 = float(input("Enter the 2nd number = "))

    if operation == "+":
        print("The entered operation is \"+\"  ")
        print("The addition of the given numbers is ",num1+num2)
    elif operation == "-":
        print("The entered operation is \"-\"  ")
        print("The subtraction of the given numbers is ",num1-num2)
    elif operation == "/":
        print("The entered operation is \"/\"  ")
        print("The division of the given number1 by number2 is ",num1/num2)
    elif operation == "*":
        print("The entered operation is \"*\"  ")
        print("The product of the given numbers is ",num1*num2)
    elif operation == "%":
        print("The entered operation is \"%\"  ")
        print("The remainder of the given number1 using number2 is ",num1%num2)
else:
    print("Enter an valid operator")