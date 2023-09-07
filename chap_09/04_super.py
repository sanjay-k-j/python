# super 
class A:
    a= "10"
    val = "theLastAirbender"
    def value(self):
        print(self.val)
class B (A):
    def getValue(self):
        print(super().a)
        super().value() # use of super

ob = B()
ob.getValue()
