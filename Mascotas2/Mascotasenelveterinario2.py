from datetime import datetime 


class Visualizador:
    """Clase que permite visualizar datos de la mascota."""

    def resumen(self):
        """Muestra los datos del objeto en formato de tabla."""
        print("|" + " | ".join(self.obtener_datos()) + "|")


class Mascota:
    """Clase base que modela una mascota en la veterinaria."""

    def __init__(self, nombre, edad, raza):
        """Inicializa los atributos principales de la mascota."""
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def obtener_datos(self):
        """Devuelve los datos principales de la mascota como lista."""
        return [
            self.__class__.__name__,
            self.nombre,
            f"{self.edad} años",
            self.raza,
            self.fecha_ingreso,
        ]


class Perro(Mascota, Visualizador):
    """Clase Perro que hereda de Mascota y Visualizador."""
    pass


class Gato(Mascota, Visualizador):
    """Clase Gato que hereda de Mascota y Visualizador."""
    pass


def ingresar_mascota():
    """Función principal para ingresar y mostrar las mascotas."""
    mascotas = []

    while True:
        try:
            cantidad = int(input("¿Cuántas mascotas va a ingresar? "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    for i in range(1, cantidad + 1):
        while True:
            print(f"Mascota {i}, ¿qué clase es (P)erro o (G)ato?")
            tipo = input().strip().lower()
            if tipo == "p":
                clase = Perro
                break
            if tipo == "g":
                clase = Gato
                break
            print("Entrada inválida. Debe ser 'P' o 'G'. Intente nuevamente.")

        nombre = input(f"¿Cuál es el nombre del {clase.__name__}? ")

        while True:
            try:
                edad = int(input(f"¿Qué edad tiene '{nombre}'? "))
                break
            except ValueError:
                print("Edad inválida. Ingrese un número.")

        raza = input(f"¿De qué raza es '{nombre}'? ")

        mascota = clase(nombre, edad, raza)
        mascotas.append(mascota)

    print("\nResumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    for mascota in mascotas:
        mascota.resumen()


if __name__ == "__main__":
    ingresar_mascota()


