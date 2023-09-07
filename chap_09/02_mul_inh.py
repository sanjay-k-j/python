# Multiple Inheritance 
class A :
    comp = "Google "
    a = "10"
class B :
    comp = "Youtube "
    b="Yes"
    def callME(self):
        print(" Call me when you want "+self.b)
class C (A,B): # They are in priority of the attribute passed 
    c="welcome"

objC = C ()
print(objC.comp) #priority
objC.callME()