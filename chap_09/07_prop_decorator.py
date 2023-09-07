# Property decorators
class Employee :
    sal = 5000
    bonus = 500

    @property
    def totalSal(self):
        return self.bonus + self.sal
        # generate result
    @totalSal.setter # sets the value of bonus 
    def totalSal(self,val):
        self.bonus = val - self.sal
e = Employee()
print(e.totalSal)
e.totalSal = 5800
print(e.sal)
print(e.bonus)

    