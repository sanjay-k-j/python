# static method 
# @static method is used when you don't 
#wants to use self as an argument  and no other arguments are passed 
class Emp:
    company = "Google"
    def getSalary(self):
        print(f"salary is of this employee working in {self.company} is {self.sal}")
    @staticmethod
    def greet ():
        print(f"hi nice to meet you ")
    def greetAgain (ajan):
        print(ajan)

sanjay = Emp()
sanjay.sal = 2000000 
ajan = "nfdfhiifdnsj"
sanjay.getSalary() # Emp.getSalary(sanjay)  are same 
sanjay.greet()
sanjay.greetAgain()