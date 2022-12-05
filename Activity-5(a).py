'''
Write a Program using function to create a user defined List.
1. Search an element also find the no of occurances of that element. 
2. Find the Index at which the element was found first. 
'''

def userDefinedList():
    l = list()
    x = int(input("Enter the no of elements in the List: "))
    for i in range(x):
        ele = int(input(f"Enter the {i} element: "))
        l.append(ele)
    
    return l

def searchElement(list, elementToSearch):
    global temp
    global count
    for i in range(len(list)):
        if (list[i] == elementToSearch):
            count += 1
            if count == 1:
                temp = list.index(elementToSearch)
    
    return count

a = userDefinedList()
print(a)
num = int(input("Enter the element to be searched: "))
temp = 0
count = 0

result = searchElement(a,num)
if count == 0:
    print(f"The {num} is not present in the list")
else:
    print(f"The {num} is present {result} times and the first occurance was at index {temp}")