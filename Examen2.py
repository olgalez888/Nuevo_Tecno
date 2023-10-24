class Producto:
    productos = {}  # Diccionario para almacenar los productos

    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None  # Inicializar en None

    @classmethod
    def crear_producto(cls, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        producto = cls(id, nombre, descripcion, costo, cantidad)
        producto.asignar_precio_de_venta(margen_de_venta)
        cls.productos[id] = producto  # Guardar el producto en el diccionario
        return producto

    def asignar_precio_de_venta(self, margen_de_venta):
        if margen_de_venta <= 0:
            print("Margen de venta debe ser mayor que 0.")
        else:
            self.precio_de_venta = self.costo / (1 - margen_de_venta)

    @classmethod
    def listar_productos(cls):
        print("Listado de Productos:")
        for id, producto in cls.productos.items():
            print(f"ID: {producto.id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Costo: {producto.costo}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Precio de Venta: {producto.precio_de_venta}")
            print("-" * 20)

# Ejemplo de uso:
producto1 = Producto.crear_producto(1, "Dona", "Dona de chocolate", 5.0, 100, 0.2)
producto2 = Producto.crear_producto(2, "Pan", "Pan con chocolate", 50.0, 50, 0.1)

Producto.listar_productos()