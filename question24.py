#Write a program that acts as a simple calculator. It should take two numbers and an operator
#  (+, -, *, /) as input and print the result.

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))

oper =  input("enter the operator + ,-,*,/ : ")


def calculator(num1,num2,oper) :
    if oper == '+':
        ans = num1 + num2
    elif oper == '-':
        ans = num1-num2
    elif oper == '*':
        ans = num1*num2 
    elif oper == '/':
        ans = num1/num2     

    print(ans)          

calculator(num1,num2,oper)
