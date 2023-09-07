# use of self 
# self is used to access all the class and instance attribute in a object
class Emp:
    company = "Google"
    def getSalary(self):
        print(f"salary is of this employee working in {self.company} is {self.sal}")
sanjay = Emp()
sanjay.sal = 2000000 
sanjay.getSalary() # Emp.getSalary(sanjay)  are same 