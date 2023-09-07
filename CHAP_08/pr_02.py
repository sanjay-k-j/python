# programmer  
class Programmer :
    company = "Mycrosoft"
    def __init__(self,name,product) :
        self.name=name 
        self.product=product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product} ")

s= Programmer("Sanjay","Skype")
s.getInfo()
j= Programmer("Saneeth","chain")
j.getInfo()


