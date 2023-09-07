# factorial of anumber 
def factorial(n):
    if n==1 or n==0:
        return 1 
    return n* factorial(n-1) 
print("the factorial of 5 is " ,factorial(5))