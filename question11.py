# Write a python program that generates the first n numbers in the Fibonacci sequence.

n = int(input("enter the number of digits needed in fibonacci : "))

def fiboSeq(n) :
    list = [0,1]
    count = 2
    while count<n :
        appd = list[count-2] + list[count-1]
        count += 1
        list.append(appd)
    print(list)

fiboSeq(n)

