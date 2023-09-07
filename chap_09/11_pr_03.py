# add vectors and multiply vectors 
class Vector():
    def __init__(self,vec):
        self.vec = vec
    def __str__(self) :
        str1 = ""
        index = 0
        for i in self.vec :
            str1 += f"{i}a{index} +"
            index +=1
        return str1[:-1]
    def __add__(id,vec2):
        newList = []
        for i in range(len(id.vec)) :
            newList.append(id.vec[i]+vec2.vec[i])
        return Vector(newList)
    def __mul__(self,vec2):
        newList = []
        for i in range(len(self.vec)) :
            newList.append(self.vec[i] * vec2.vec[i])
        return Vector(newList)
v1 = Vector([1,2])
v2 = Vector([11,22])
print(v1 + v2)
print(v1*v2)
    