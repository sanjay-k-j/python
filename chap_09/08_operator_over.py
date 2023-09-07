# operator overloading 
class Number:
    def __init__(self , num) :
        self.num = num 
    def __add__(self, num2) :
        print("Lets Add")
        return self.num + num2.num
    def __mul__(self , num3):
        print("Multiply")
        return self.num * num3.num
n1 = Number(10)
n2 = Number(20)
sum = n1+n2 # Overloading the operator
mul = n1 * n2
print(sum)
print(mul)