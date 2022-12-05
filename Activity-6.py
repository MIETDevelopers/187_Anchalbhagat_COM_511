n = int(input('\nEnter the number of students : '))
dict = {}
for i in range(n):
    rno = input(f"\nRoll No for student {i+1} : ")
    m = []
    for j in range(3):
        markss = float(input(f'Marks for subject {j+1} :'))
        m.append(markss)
    dict[rno] = m
print(f'\nDictionary:\n{dict}')

rno = input("\nEnter the Roll No whose record to be searched: ")
for items in dict:
    if items == rno:
        print(dict.get(items))
        break
else:
    print("Data not Exists")

print("\nRecords of all students with percentages greater than 60 are:-")
for items in dict:
    x=dict.get(items)
    percent = sum(x)/3
    if percent > 60:
        print(items ,"->", dict.get(items))