# constructor is called automatically when the object is created 
class sanj:
    def __init__(self,a,b,c) :
        self.a=a
        self.b=b
        self.c=c
        print("Automatic ")

    def details (self):
        print(f"a is = {self.a}")
        print(f"b is = {self.b}")
        print(f"c is = {self.c}")
# s=sanj()-> throws an error 
# s.details(10,20,30) 
s = sanj(10,20,30) 
s.details()