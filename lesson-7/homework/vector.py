import math
class Vector:
    def __init__(self, *args):
        self.args = args
    def __add__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError("Vectors must be in the same dimension")
        return Vector(*(a+b for a, b in zip(self.args, other.args)))
    def __sub__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError("Vectors must be in the same dimension")
        return Vector(*(a - b for a , b in zip(self.args, other.args)))
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.args) != len(other.args):
                raise ValueError("Vectors must be of same dimension for dot product")
            return sum(a * b for a, b in zip(self.args, other.args))
        elif isinstance(other, (int, float)):
            return Vector(*(other * x for x in self.args))
        else:
            raise TypeError("Unsupported operand types")
    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.args))
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(x / mag for x in self.args))
    def __str__(self):
        return f"Vector({', '.join(str(x) for x in self.args)})"
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)
v3 = v1 + v2
print(v3) 
v4 = v2 - v1
print(v4)
dot_product = v1 * v2
print(dot_product)
v5 = 3 * v1
print(v5) 
print(v1.magnitude())
v_unit = v1.normalize()
print(v_unit) 