# intro_to_python_assignment
introduction to python assignment


def calculator():
    number1=float(input("enter an number: "))
    number2= float (input("input another number: "))
    operator = input("enter operator: ")
   

    if operator=='+':
        print("answer is ", number1+number2)
    elif operator=='/':
        print("answer is ",number1/number2)
    elif operator=='-':
        print ("answer is ",number1-number2)
    elif operator=='*':
        print("answer is ",number1*number2)
    else:
        print("invalid input try again: ")

calculator()
OR


num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
operation = input("input operation: ")

if operation== "+":
     print("answer is ",num1+num2)
elif operation == "*":
     print("answer is ",num1*num2)
elif operation=="/":
     print("answer is ",num1/num2)
elif operation=="-":
     print("answer is ",num1-num2)
else:print("invalid input, try again")

