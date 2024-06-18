#Write a program in python that checks if a 
# string starts with a given prefix or ends with a given suffix.

str = input("enter the string : ")

prefix = "so"
suffix = "de"

len_pref = len(prefix)
len_suff = len(suffix)

def  checkPrefix(str) :
    if str[:len_pref] == prefix :
        print("it contains prefix")
    else:
        print("it doesnt contain prefix")


def checkSuffix(str) :
    if str[-len_suff :] == suffix :
        print("it contains the given suffix")
    else :
        print("it doesnt contain the given suffix")


checkPrefix(str)
checkSuffix(str)

