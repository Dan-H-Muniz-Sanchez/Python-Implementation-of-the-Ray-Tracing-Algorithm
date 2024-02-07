import math


class Vector:
    """ESTA CLASE NOS AYUDARA A CREAR UNA ESTRUCTURA DE VECTOR EN |R^3 """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z #CONSTRUCTOR

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def dot_product(self, other): #OPERACION PRODUCTO PUNTO
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self): #OPERACION MAGNITUDE
        return math.sqrt(self.dot_product(self))

    def normalize(self): #NORMALIZACION DE UN VECTOR
        return self / self.magnitude()

    def __add__(self, other): #SUMAR DOS VECTORES
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other): #RESTAR DOS VECTORES
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other): #OPERACION MULTIPLICACION
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)