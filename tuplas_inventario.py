# Sistema de inventario con tuplas

# 1. Inicializar una tupla vacía para productos
productos = ()
print(f"1. Tupla inicial (vacía): {productos}\n")

# 2. Agregar productos como tuplas (código, nombre, precio, cantidad)
productos = (
    ("P001", "Laptop", 15000.50, 10),
    ("P002", "Mouse", 450.00, 50),
    ("P003", "Teclado", 700.75, 30),
    ("P004", "Monitor", 4500.00, 15),
    ("P005", "Webcam", 950.25, 25)
)
print("2. Inventario inicial de productos:")
print(productos)
print("-" * 30)

# 3. Usar slicing para mostrar los primeros 3 productos
primeros_tres = productos[:3]
print("3. Primeros 3 productos del inventario:")
print(primeros_tres)
print("-" * 30)

# 4. Modificar el precio del segundo producto (creando una nueva tupla)
print("4. Modificando el precio del segundo producto ('Mouse')...")
# Creamos la nueva tupla para el 'Mouse' con el precio actualizado (de 450.00 a 499.99)
producto_modificado = (productos[1][0], productos[1][1], 499.99, productos[1][3])

# Recreamos la tupla completa de productos usando slicing y concatenación
productos = productos[:1] + (producto_modificado,) + productos[2:]
print("Inventario con el precio del 'Mouse' actualizado:")
print(productos)
print("-" * 30)

# 5. Ordenar productos por precio (ascendente y descendente)
print("5. Ordenando productos por precio...")

# Orden ascendente
productos_ascendente = sorted(productos, key=lambda producto: producto[2])
print("\nProductos ordenados por precio (ascendente):")
print(productos_ascendente)

# Orden descendente
productos_descendente = sorted(productos, key=lambda producto: producto[2], reverse=True)
print("\nProductos ordenados por precio (descendente):")
print(productos_descendente)
print("-" * 30)

# 6. Eliminar el último producto con slicing
# Creamos una nueva tupla que incluye todos los elementos excepto el último.
print("6. Eliminando el último producto del inventario...")
productos_sin_ultimo = productos[:-1]
print("Inventario sin el último producto:")
print(productos_sin_ultimo)