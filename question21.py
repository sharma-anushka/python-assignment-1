#Write a python program that counts the occurrences of a specific element in a list.

list = [1,2,22,2,33,4,2,5,6,7,2,89,90]

spcElem = 2
idx = 0
count =0
listlen = len(list)
while idx< listlen :
    if list[idx] == spcElem :
        count +=1
    idx +=1

print(count)        