#find harry
post =input("Enter the post\n")
li =list(post.split(" "))
k=1
for i in li:
    if i.lower() == "harry" :
        print("The post is related to harry")
        k=0
if(k==1):
    print("not harry related")


