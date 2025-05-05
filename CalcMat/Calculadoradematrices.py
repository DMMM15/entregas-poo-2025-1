David Mateo Moyano Mahecha

class Matriz:
    """Clase para representar y operar matrices 2x2."""

    def __init__(self, elementos):
        self.valores = elementos 

    def __add__(self, otra):
        return Matriz([
            [self.valores[0][0] + otra.valores[0][0],
             self.valores[0][1] + otra.valores[0][1]],
            [self.valores[1][0] + otra.valores[1][0],
             self.valores[1][1] + otra.valores[1][1]]
        ])

    def __sub__(self, otra):
        return Matriz([
            [self.valores[0][0] - otra.valores[0][0],
             self.valores[0][1] - otra.valores[0][1]],
            [self.valores[1][0] - otra.valores[1][0],
             self.valores[1][1] - otra.valores[1][1]]
        ])

    def __mul__(self, otra):
        a, b = self.valores, otra.valores
        return Matriz([
            [a[0][0]*b[0][0] + a[0][1]*b[1][0],
             a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0],
             a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ])

    def mostrar(self, etiqueta="Matriz"):
        print(f"{etiqueta}:")
        print(f"|{self.valores[0][0]}  {self.valores[0][1]}|")
        print(f"|{self.valores[1][0]}  {self.valores[1][1]}|")


def leer_matriz(numero):
    print(f"\nIngrese valores para la matriz {numero}:")
    elementos = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"Matriz {numero}: elemento {i},{j} > "))
            fila.append(valor)
        elementos.append(fila)
    return Matriz(elementos)


def main():
    m1 = leer_matriz(1)
    m2 = leer_matriz(2)

    print()
    m1.mostrar("Matriz 1")
    m2.mostrar("Matriz 2")

    print("""
> Escriba 1 para suma,
>         2 para resta,
>         3 para multiplicación
    """)
    opcion = input("< ")

    if opcion == "1":
        resultado = m1 + m2
        print("\n> La suma de las dos matrices es:")
        resultado.mostrar()
    elif opcion == "2":
        resultado = m1 - m2
        print("\n> La resta de las dos matrices es:")
        resultado.mostrar()
    elif opcion == "3":
        resultado = m1 * m2
        print("\n> El producto de las dos matrices es:")
        resultado.mostrar()
    else:
        print("> Opción no válida.")


if __name__ == "__main__":
    main()
