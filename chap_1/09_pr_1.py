# marks of students 
a=[]
n=int(input("Enter the no of students"))
for i in range(0,n):
    k=str(i+1)
    l=int(input("Enter the marks of the student "+k+" "))
    a.append(l)
a.sort()
print(a)