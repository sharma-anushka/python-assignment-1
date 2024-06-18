#Write a python program that checks if two strings are anagrams of each other.

str1 = input("enter the first string : ")
str2 = input("enter the second string : ")

lst1 =  list(str1)
lst2 = list(str2)

lst1_sorted = lst1.sort()
lst2_sorted = lst2.sort()

if lst1_sorted == lst2_sorted :
    print("true")
else:
    print("false")