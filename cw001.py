#Take input of two numbers and an oparator (+,-,*,/) and print the result.

a=float(input("Input first number..."))
b=float(input("Input second number..."))
opr=str(input("Input an oparatot..."))

if (opr=='+'):
    print("Result: ",a+b)
elif(opr=='-'):
    print("Result: ",a-b)
elif(opr=='*'):
    print("Result: ",a*b)
elif(opr=='/'):
    if (b==0):
        print("Can't be devided by Zero.")
    else:
        print("Result: ",a/b)
else:
    print("Oh no! Invalid Input.")