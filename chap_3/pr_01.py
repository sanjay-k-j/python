# subject marks 
l=[]
sm=0
fail=1
for i in range(0,3):
    k=input("Enter the marks of the subject"+str(i+1)+" ")
    l.append(k)
    if(int(l[i]) <33):
        print("you are failed in subject",i+1)
        fail = 0
    sm=int(l[i])+sm

if sm/3 <40 and fail==1 :
    print("You are failed due to avg less than 40 ")
elif fail == 1:
    print("Congratulatons you are passed ")
