class Producto:
    def __init__(self, nombre, precio_unitario, cantidad):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def mostrar_datos(self):
        # Muestra los datos del producto
        print(f"Nombre del producto: {self.nombre}")
        print(f"Precio unitario: ${self.precio_unitario:.2f} COP")
        print(f"Cantidad en stock: {self.cantidad} unidades")
        print("-" * 30)


def obtener_producto():
    # Función para obtener los datos de un producto
    nombre = input("Ingrese el nombre del producto: ")
    precio_unitario = float(input("Ingrese el precio unitario en COP: "))
    cantidad = int(input("Ingrese la cantidad de unidades: "))
    return Producto(nombre, precio_unitario, cantidad)


def main():
    # Creamos una lista para almacenar los productos
    productos = []

    print("Bienvenido al sistema de inventario de la tienda.\n")

    # Recopilamos los datos de tres productos
    for i in range(1, 4):
        print(f"\nProducto {i}:")
        producto = obtener_producto()
        productos.append(producto)

    # Mostramos los datos de los tres productos
    print("\nDatos de los productos ingresados:")
    for producto in productos:
        producto.mostrar_datos()


# Llamamos a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
