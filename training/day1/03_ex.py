# Write a program to cyclically rotate an array by one
arr=[int(i) for i in input("Enter the list : ").split()]


def cyclically_rotate(arr):
    # get the last element of the array
    last = arr[-1]
    
    # shift each element one position to the right
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
        
    # put the last element at the first position
    arr[0] = last
    
    return arr


rotate = True
while rotate :
    print("The array after cyclically rotated by one is :" )
    print(cyclically_rotate(arr))
    ter=input('''do it again "y" , exit "n" ''')
    if(ter=="n"):
        exit()
