# # put negative numbers to one side of the list 
# arr=[43,3423,343,234,-34,34,-322,45,3,-43]

# def bubble_sort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n):
#         # Last i elements are already sorted
#         for j in range(0, n-i-1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print(bubble_sort(arr))


arr=input("Enter the list :").split()
int_arr=[int(i) for i in arr]
newArr=[]
for i in int_arr:
    if(i<0):
        newArr.append(i)
for i in int_arr:
    if(i>0):
        newArr.append(i)
print(newArr)