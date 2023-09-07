# calculator 
class Calci:
    def __init__(self,num) :
        self.number = num
    def square (self):
        print(f"The square of the {self.number} is {self.number**2}")
    def squareRoot (self):
        print(f"The squareroot  of the {self.number} is {self.number**0.5}")
    def cube (self):
        print(f"The cube of the {self.number} is {self.number**3}")
ob = Calci(10)
ob.square()
ob.squareRoot()
ob.cube()