# Write a python program that calculates the factorial of a given number.

num = int(input(" enter the number you want to find factorial of : "))
fact = 1
while(num > 0) :
    fact = fact* (num)
    num = num-1

print("the factorial is :" , fact)

