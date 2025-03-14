"David Mateo Moyano Mahecha"

class Producto:
    """Clase que modela un producto de la tienda."""

    def __init__(self, nombre: str, precio: int, cantidad: int,
                 descripcion: str, clasificacion: str):
        """Inicializa un producto con sus atributos principales."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def __str__(self):
        """Devuelve una representación en texto del producto."""
        return (f"| {self.nombre:<8} | {self.cantidad:<10} unidades | "
                f"{self.precio:<8} pesos | {self.descripcion[:15]:<15} | "
                f"{self.clasificacion:<12} | {self.inventario_precio():<15} "
                f"pesos | {self.calcula_precio(5):<10} pesos |")

    def calcula_precio(self, cantidad: int) -> int:
        """Calcula el precio total por la cantidad especificada."""
        return self.precio * cantidad

    def inventario_precio(self) -> int:
        """Devuelve el valor total de los productos en el inventario."""
        return self.precio * self.cantidad


def solicitar_producto(numero: int) -> Producto:
    """Solicita los datos de un producto al usuario y devuelve un objeto."""
    nombre = input(f"\n> Producto {numero}, ¿cuál es el nombre?\n< ").strip()
    precio = int(input(f"> ¿Cuál es el precio de '{nombre}'?\n< "))
    cantidad = int(input(f"> ¿Qué cantidad hay de '{nombre}'?\n< "))
    descripcion = input(f"> Introduzca la descripción de '{nombre}':\n< ").strip()
    clasificacion = input(f"> ¿Qué clasificación tiene '{nombre}'? ej: alimentacion, aseo, etc...\n< ").strip()

    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def calcular_precio_unitario_por_clasificacion(productos):
    """Suma los precios unitarios de los productos por clasificación."""
    resumen = {}

    for producto in productos:
        resumen[producto.clasificacion] = (
            resumen.get(producto.clasificacion, 0) + producto.precio
        )

    return resumen


def main():
    cantidad_productos = int(input("\n> ¿Cuántos productos va a ingresar?\n< "))
    productos = [solicitar_producto(i) for i in range(1, cantidad_productos + 1)]

    print("\n> Resumen:")
    print("> | Producto | Cantidad    | Precio   | Descripción     "
          "| Clasificación  | Total en inventario | Precio x5 unidades |")
    print("> " + "-" * 110)

    for producto in productos:
        print("> " + str(producto))

    resumen_clasificacion = calcular_precio_unitario_por_clasificacion(productos)

    print("\n> Precios por clasificación")
    print("> | Clasificación  | Precio Unitario Total |")
    print("> " + "-" * 40)

    for clasificacion, total in resumen_clasificacion.items():
        print(f"> | {clasificacion:<13} | {total:<21} pesos |")


if __name__ == "__main__":
    main()
