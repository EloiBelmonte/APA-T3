"""
____________________________________
| Creación de nuestra Clase Vector |
|__________________________________|
"""


class Vector:

    # vector = list()
    # vector = [] es lo mismo

    #__new__() crea el constructor
    # __init__() constructor que se usa normalmente
    
    # Constructor
    def __init__(self, iterable):
        self.vector = [elemento for elemento in iterable]

    # Representación "oficial" (para depuración)
    def __repr__(self):
        return "Vector(" + repr(self.vector) + ")"

    # Representación para imprimir
    def __str__(self):
        return str(self.vector)

    # Multiplicación: escalar o Hadamard
    def __mul__(self, other):
        # Caso 1: vector * vector
        if isinstance(other, Vector):
            return Vector([a * b for a, b in zip(self.vector, other.vector)])
        
        # Caso 2: vector * escalar
        else:
            return Vector([a * other for a in self.vector])

    # Para permitir: escalar * vector
    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        if isinstance(other, Vector):
            return sum(a * b for a, b in zip(self.vector, other.vector))
        else:
            raise TypeError("El operador @ solo está definido entre vectores")


    def __floordiv__(self, other):
        if isinstance(other, Vector):
            numerador = self @ other
            denominador = other @ other
            escalar = numerador / denominador
            return escalar * other
        else:
            raise TypeError("El operador // requiere otro vector")


    def __mod__(self, other):
        if isinstance(other, Vector):
            paralelo = self // other
            return Vector([a - b for a, b in zip(self.vector, paralelo.vector)])
        else:
            raise TypeError("El operador % requiere otro vector")


if __name__ == "__main__":
    # Test multiplicación
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    
    print("v1 * 2 =", v1 * 2)
    print("2 * v1 =", 2 * v1)
    print("v1 * v2 =", v1 * v2)

    assert (v1 * 2).vector == [2, 4, 6]
    assert (2 * v1).vector == [2, 4, 6]
    assert (v1 * v2).vector == [4, 10, 18]
    print("Multiplicación OK")

    # Test producto escalar
    print("v1 @ v2 =", v1 @ v2)
    
    assert v1 @ v2 == 32
    print("Producto escalar OK")

    # Test componentes
    v1 = Vector([2, 1, 2])
    v2 = Vector([0.5, 1, 0.5])

    paralelo = v1 // v2
    perpendicular = v1 % v2

    print("v1 // v2 =", v1 // v2)
    print("v1 % v2 =", v1 % v2)

    assert paralelo.vector == [1.0, 2.0, 1.0]
    assert perpendicular.vector == [1.0, -1.0, 1.0]

    print("Componentes OK")

    print("TODOS LOS TESTS PASADOS")
