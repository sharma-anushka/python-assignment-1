#Write a python program that takes a list of numbers and returns their sum.

list = [1,2,3,4,5,6,7,8,90]
lstlen = len(list)
def sumList(list) :
    sum = 0 
    idx = 0
    while(idx < lstlen):
        sum += list[idx]
        idx +=1
    print(sum)
sumList(list)    