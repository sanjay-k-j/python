# find the greatest of  3 numbers
def great (a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        return b
    return c
print("the greatest of a b and c is ",great (10,-62,0))