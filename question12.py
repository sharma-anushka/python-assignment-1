#Write a python program that calculates the sum of the digits of a given number.

num = int(input("enter the number : "))

sum = 0
while num > 0:
    digit = num % 10
    digit = int(digit)
    sum += digit
    num /= 10
    num = int(num)

print("the sum of digits is : ", sum)
