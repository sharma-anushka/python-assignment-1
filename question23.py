#Write a program that converts temperature from
#Celsius to Fahrenheit and vice versa based on user input.

choice = int(input("enter 0 if you want to convert C to F and 1 for vice versa : "))

temp = int(input("enter the temperature to be converted : "))

if choice == 0:
    ans = (temp * (9/5)) +32

if choice == 1:
    ans = (temp -32) * 5 /9 

print(ans)