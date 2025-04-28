David Mateo Moyano mahecha

class Visualizador:
    """Clase que permite visualizar datos de la mascota."""

    def resumen(self):
        """Muestra los datos del objeto en formato de tabla."""
        print("|" + " | ".join(self.obtener_datos()) + "|")


class Mascota:
    """Clase base que modela una mascota en la veterinaria."""

    def __init__(self, nombre, edad, raza):
        """ los atributos principales de la mascota."""
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def obtener_datos(self):
        """Devuelve los datos principales de la mascota en lista."""
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
    cantidad = int(input("¿Cuántas mascotas va a ingresar? "))

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
        edad = int(input(f"¿Qué edad tiene '{nombre}'? "))
        raza = input(f"¿De qué raza es '{nombre}'? ")

        mascotas.append(clase(nombre, edad, raza))

    print("\nResumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    for mascota in mascotas:
        mascota.resumen()


if __name__ == "__main__":
    ingresar_mascota()
