# union and intersection
list1 = [int(item) for item in input("Enter the list 1 items : ").split()]
list2 =[int(item) for item in input("Enter the list 2 itemms : ").split()]
inter=[]
for i in list1:
    if i in list2:
        inter.append(i)
print("the intersection of list is : ",inter)
for i in list1:
    if i not in list2:
        list2.append(i)
print("the union of lists ",list2)