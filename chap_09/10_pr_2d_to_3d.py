# 2D to 3D vector 
class ve2d:
    def __init__(self,i,j) :
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class ve3d(ve2d):
    def __init__(self, i, j ,k):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

ob = ve2d(4,5)
ob2 = ve3d(4,6,8)
print(ob)
print(ob2)