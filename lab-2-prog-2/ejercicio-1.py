import math
class Mipunto: 
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y 
    def distancia(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    def distacia_xy(self,x,y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
    
p1 = Mipunto()           
p2 = Mipunto(10, 30.5)   
print("Distancia:", p1.distancia(p2))