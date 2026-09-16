import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        suma_x = self.x + other.x
        suma_y = self.y + other.y
        suma_z = self.z + other.z
        return AlgebraVectorial(suma_x, suma_y, suma_z)

    def __sub__(self, other):
        resta_x = self.x - other.x
        resta_y = self.y - other.y
        resta_z = self.z - other.z
        return AlgebraVectorial(resta_x, resta_y, resta_z)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __mul__(self, other):
        producto_x = self.x * other.x
        producto_y = self.y * other.y
        producto_z = self.z * other.z
        return producto_x + producto_y + producto_z

    def __xor__(self, other):
        cruz_x = self.y * other.z - self.z * other.y
        cruz_y = self.z * other.x - self.x * other.z
        cruz_z = self.x * other.y - self.y * other.x
        return AlgebraVectorial(cruz_x, cruz_y, cruz_z)

    def es_casi_cero(self, valor):
        return abs(valor) < 0.000001

    def verificar_perpendicular_a(self, other):
        suma = self + other
        resta = self - other
        diferencia = abs(suma) - abs(resta)
        return self.es_casi_cero(diferencia)

    def verificar_perpendicular_b(self, other):
        resta_1 = abs(self - other)
        resta_2 = abs(other - self)
        diferencia = resta_1 - resta_2
        return self.es_casi_cero(diferencia)

    def verificar_perpendicular_c(self, other):
        producto = self * other
        return self.es_casi_cero(producto)

    def verificar_perpendicular_d(self, other):
        suma = self + other
        lad_iz = abs(suma) ** 2
        modulo_propio = abs(self) ** 2
        modulo_other = abs(other) ** 2
        lad_der = modulo_propio + modulo_other
        diferencia = lad_iz - lad_der
        return self.es_casi_cero(diferencia)

    def verificar_paralela_e(self, other):
        if other.x != 0 and other.y != 0 and other.z != 0:
            razon_x = self.x / other.x
            razon_y = self.y / other.y
            razon_z = self.z / other.z
            iguales_1 = self.es_casi_cero(razon_x - razon_y)
            iguales_2 = self.es_casi_cero(razon_x - razon_z)
            return iguales_1 and iguales_2
        return False

    def verificar_paralela_f(self, other):
        producto_cruz = self ^ other
        cruz_x_cero = self.es_casi_cero(producto_cruz.x)
        cruz_y_cero = self.es_casi_cero(producto_cruz.y)
        cruz_z_cero = self.es_casi_cero(producto_cruz.z)
        return cruz_x_cero and cruz_y_cero and cruz_z_cero

    def calcular_proyeccion_sobre(self, other):
        producto_punto = self * other
        modulo_other = abs(other)
        modulo_cuadrado = modulo_other ** 2
        factor = producto_punto / modulo_cuadrado
        proyeccion_x = factor * other.x
        proyeccion_y = factor * other.y
        proyeccion_z = factor * other.z
        return AlgebraVectorial(proyeccion_x, proyeccion_y, proyeccion_z)

    def calcular_componente_en(self, other):
        producto_punto = self * other
        modulo_other = abs(other)
        return producto_punto / modulo_other

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
a = AlgebraVectorial(1, 0, 0)
b = AlgebraVectorial(0, 1, 0)

print("a) ¿Perpendicular?", a.verificar_perpendicular_a(b))
print("b) ¿Perpendicular?", a.verificar_perpendicular_b(b))
print("c) ¿Perpendicular?", a.verificar_perpendicular_c(b))
print("d) ¿Perpendicular?", a.verificar_perpendicular_d(b))

c = AlgebraVectorial(2, 4, 6)
d = AlgebraVectorial(1, 2, 3)
print("e) ¿Paralela?", c.verificar_paralela_e(d))
print("f) ¿Paralela?", c.verificar_paralela_f(d))

print("Proyección:", a.calcular_proyeccion_sobre(b))
print("Componente:", a.calcular_componente_en(b))