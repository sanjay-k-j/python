#set is a collection of non repetative elements
# set is immutable
a={1,34,5,53,23,4543}
print(a)
print(type(a))

b={3,3,4}
print(b)

# empty dictionary 
a={}
print(type(a))

#empty set
c=set()
print(type(c))
c.add(34) #adds elements to the set 


# set methods
# immutable thats y we can add tuples but not lists
c.add(4)
print(c)
#c.add([432,543,533])# cannot add list or dictionary

c.remove(4)
c.add(5)
print(c) 
c.add((343,534,54,5345))

print(c) 
k=c.pop() # removes an orbitory elements in set and returns that value
print(k)
print(len(b))
#c.clear()  empty the set 
print(c)
