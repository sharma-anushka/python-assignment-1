#Write a python program that checks if a substring is present in a given string.

str = "shakalakaboomboom"

substr = input("enter the substring you want to check : ")

if substr in str :
    print("the sub string is present in " ,str)
else :
    print("the substring is not present in " ,str)