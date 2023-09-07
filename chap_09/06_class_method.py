# class method 

class Emp :
    comp = "Youtube"
    sal = 100
    # def changeSal(self):
    #     self.__class__.sal = 2000
    # this will change the value of the class attribute 
    # normally an object created (instance attributes ) create a replica of the value in the object only
    @classmethod
    def changeSal(self,a):
        self.sal = a
e = Emp()
print(e.sal)
e.changeSal(30)
print(e.sal)
print(Emp.sal) # class attribute value changed 