l=[]
#greatest number 
gr=0
for i in range(0,4):
    j=input("Enter the number"+str(i+1)+" ")
    l.append(j)
    
    if (gr <int(l[i]) ):
        gr=int(l[i])
    
print(gr, "is the greatest number")



    