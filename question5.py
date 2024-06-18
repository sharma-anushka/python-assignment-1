#Write a program that takes a string input from the user and writes it to a text file.

str = input("enter a string : ")
sample_file = open("D:\python assignment 1\random.txt" , 'w')

print("the string is : " , str , file=sample_file)