'''
Write a Program using function to Create a userdefined 2D Matrix.
1. Search an element also find the no of occurances of that element. 
2. Find the Index at which the element was found first. 
'''

def matrix():
    l1 = []
    rows = int(input("Enter the no of rows in the Matrix: "))
    columns = int(input("Enter the no of columns in the Matrix: "))
    print("\n")
    for i in range(rows):
        l2 = []
        for j in range(columns):
            ele = int(input(f"Enter the {i}{j} element of Matrix: "))
            l2.append(ele)
        l1.append(l2)

    return l1

def searchElement(list, elementToSearch):
    global count
    global temp1
    global temp2

    for i in range(len(list)):
        for j in range(len(list)):
            if (list[i][j] == elementToSearch):
                count += 1

                if(count == 1):
                    temp1 = i
                    temp2 = j

    return count

result1 = matrix()
print(result1)

count = 0
temp1 = 0
temp2 = 0

num = int(input("Enter the element to be searched: "))
result2 = searchElement(result1, num)
if count == 0:
    print(f"{num} is not present in the list")
else:
    print(f"{num} is present {result2} times and the first occurance was at index {temp1},{temp2}")