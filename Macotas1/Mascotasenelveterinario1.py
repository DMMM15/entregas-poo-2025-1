David Mateo Moyano Mahecha

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def obtener_datos(self):
        return [
            self.__class__.__name__,
            self.nombre,
            f"{self.edad} años",
            self.raza,
            self.fecha_ingreso,
        ]


class Perro(Mascota):
    pass


class Gato(Mascota):
    pass


def ingresar_mascota():
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

    print("Resumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    for mascota in mascotas:
        print("|" + " | ".join(mascota.obtener_datos()) + "|")


if __name__ == "__main__":
    ingresar_mascota()
