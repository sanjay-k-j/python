# Inheritance ,  overwrite 
# example for single inheritance 
class Employee:
    comp = "Google"
    def getDetails(self):
        print("This is an Employee ")

class Programmer (Employee): # Inherit the class Employee 
    comp = " Youtube " # Overwrite 
    lang= "Python" # create own attibutes 
    def getDetails(self):
        print("this is a programmer ")
    def companayDetails(self):
        print(f"The name of the company in {self.comp} ")

p = Programmer()
e = Employee()
e.getDetails()
p.getDetails()
print(p.comp)
p.companayDetails()
