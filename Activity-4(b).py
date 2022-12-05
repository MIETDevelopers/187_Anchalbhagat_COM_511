#Program to perform Linear Search on a user defined List

def linearSearch(l,n,num):
    for i in range(0,n):
        if (l[i] == num):
            print(f"{num} is present in the List at index {i}")
            break
    else:
        print(f"{num} is not in the List.")

l = []
x = int(input("Enter the elements of List: "))
print("\n")
for i in range(x):
    ele = int(input(f"Enter {i+1} element of  list: "))
    l.append(ele)
print(l)
n = len(l)
num = int(input("\nEnter a number to be searched: "))
linearSearch(l,n,num)