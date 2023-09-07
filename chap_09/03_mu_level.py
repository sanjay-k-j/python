# Multilevel Inheritance 
'''An objects searches attributes in the respective class and it absent 
in the class in inherites from its nearest parent'''
class Person:
    country = "India "
    count = 1
    def takeBreath(self):
        print("I'm Breathing ")
class Emp (Person):
    count = 2
class work (Emp):
    x= "car"
ob = work()
print(ob.count)
print(ob.country)