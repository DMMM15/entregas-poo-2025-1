David Mateo Moyano mahecha

class Producto:
    """Clase que modela un producto de la tienda."""

    def __init__(self, nombre: str, precio: int, cantidad: int,
                 descripcion: str, clasificacion: str):
        """
        Inicializa un producto con nombre, precio unitario, cantidad,
        descripción y clasificación.

        :param nombre: Nombre del producto.
        :param precio: Precio unitario en COP.
        :param cantidad: Cantidad disponible en unidades.
        :param descripcion: Descripción breve del producto.
        :param clasificacion: Categoría del producto 
                              (Ej: alimentación, aseo, etc.).
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def __str__(self):
        """Devuelve una representación en texto del producto."""
        return (f"|{self.nombre:<15} |{self.cantidad:<10} unidades "
                f"|{self.precio:<10} pesos |{self.clasificacion:<15} "
                f"| {self.descripcion}")


def solicitar_producto(numero: int) -> Producto:
    """
    Solicita los datos de un producto al usuario y devuelve un objeto Producto.

    :param numero: Número del producto que se está registrando.
    :return: Un objeto de la clase Producto con los datos ingresados.
    """
    nombre = input(f"\n> Producto {numero}, ¿cuál es el nombre?\n< ")
    precio = int(input(f"> ¿Cuál es el precio de '{nombre}'?\n< "))
    cantidad = int(input(f"> ¿Qué cantidad hay de '{nombre}'?\n< "))
    descripcion = input(f"> Describe brevemente '{nombre}':\n< ")
    clasificacion = input("> ¿A qué categoría pertenece? "
                          "(Ej: alimentación, aseo, etc.)\n< ")

    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def calcular_precio_por_clasificacion(productos):
    """
    Calcula el precio total de los productos agrupados por clasificación.

    :param productos: Lista de objetos Producto.
    :return: Diccionario con la clasificación como clave y el total en COP.
    """
    resumen = {}

    for producto in productos:
        total_precio = producto.precio * producto.cantidad
        if producto.clasificacion in resumen:
            resumen[producto.clasificacion] += total_precio
        else:
            resumen[producto.clasificacion] = total_precio

    return resumen


def main():
    """Función principal que gestiona la recolección y visualización."""
    cantidad_productos = int(input("\n> ¿Cuántos productos deseas ingresar?\n< "))
    productos = [solicitar_producto(i) for i in range(1, cantidad_productos + 1)]

    print("\n> Resumen de productos:")
    print("> |Producto        |Cantidad   |Precio      |Clasificación    |Descripción")
    print("> " + "-" * 80)

    for producto in productos:
        print("> " + str(producto))

    resumen_clasificacion = calcular_precio_por_clasificacion(productos)

    print("\n> Resumen de precios por clasificación:")
    for clasificacion, total in resumen_clasificacion.items():
        print(f"> {clasificacion}: {total} pesos")


if __name__ == "__main__":
    main()
