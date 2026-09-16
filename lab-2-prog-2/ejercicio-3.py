import math
class Vector3D:
    def __init__(self,comp1 = 0 , comp2 = 0 , comp3 = 0):
        self.comp1 = comp1
        self.comp2 = comp2
        self.comp3 = comp3
        
    def __add__(self, other):
        c1 = self.comp1 + other.comp1
        c2 = self.comp2 + other.comp2
        c3 = self.comp3 + other.comp3
        return Vector3D (c1 ,c2 ,c3)
    
    def __mul__(self, other):
        newcomp1 = other * self.comp1
        newcomp2 = other * self.comp2
        newcomp3 = other * self.comp3
        return Vector3D(newcomp1 , newcomp2 , newcomp3)
    
    def longitud(self,):
        return  math.sqrt(
            self.comp1**2 +
            self.comp2**2 +
            self.comp3**2
            ) 
        
    def normal(self):
        return Vector3D (
                  self.comp1 / self.longitud(),
                  self.comp2 / self.longitud(),
                  self.comp3 / self.longitud()
                  )
    def escalar(self, other):
        return self.comp1 * other.comp1 + self.comp2 * other.comp2 + self.comp3 * other.comp3
    
    def vectorial(self,other):
         return Vector3D (
             self.comp2 * other.comp3 - self.comp3 * other.comp2 ,
             self.comp3 * other.comp1 - self.comp1 * other.comp3 ,
             self.comp1 * other.comp2 - self.comp2 * other.comp1 
                          )
         
    def __str__(self):
        return f"{self.comp1}, {self.comp2}, {self.comp3}"
    
a = Vector3D(2 , 3  , 4)
b = Vector3D(5 , 6  , 7)
r = 2
print("Vector a: ",a)
print("Vectro b: ",b)
print("a) Suma a + b: ",a + b)
print("b) Multiplicacion por escalar: ",a * r)
print("c) Longitud de a: ", round(a.longitud()) , 4)
print("d) Vector normalizado de a:", a.normal())
print("e) Producto escalar: ",a.escalar(b))
print("f) Producto Vectorial axb: ", a.vectorial(b))