# pattern of * in python 
n=int(input("Enter the number : ")) 
def pattern(n):
    if n==0:
        return
    print("* " * n,end="")
    print()
    pattern(n-1)
pattern(n)