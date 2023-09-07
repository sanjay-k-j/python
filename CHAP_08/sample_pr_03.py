# value of a not changes in the class instance 
class Sample:
    a="Sanjay"
obj = Sample()
obj.a = "Ajay"
print(obj.a)
print(Sample.a)
