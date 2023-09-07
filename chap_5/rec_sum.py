# write a recursive functon to print sun of n natural numbers 
n=int(input("Enter the number : ")) 
sum= 0
def sumOfN (n):
    if n==0:
        return n
    return n+sumOfN(n-1)
print("The sum of n numbers are ",sumOfN (n))