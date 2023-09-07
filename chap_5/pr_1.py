# print star
# n=int(input("Enter the number "))
# for i in range(n):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))

n=3
for i in range(n): 
  
    if i != 1 :
        print("*" * n)
    else:
        print("* *")
    # for j in range(n):
    #     if i ==2 and j==2:
    #         print(" ",end="")
    #     else:
    #         print("*",end="")