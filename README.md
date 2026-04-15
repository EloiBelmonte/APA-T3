# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Eloi Belmonte Alcalá

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Eloi Belmonte Alcalá

## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

![Ejecución de tests](./vectores1.png)
![Ejecución de tests](./vectores2.png)
![Ejecución de tests](./vectores3.png)

#### Código desarrollado

```python
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
```

#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
