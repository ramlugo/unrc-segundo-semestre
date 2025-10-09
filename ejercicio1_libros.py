# ===================================================================
# PARTE 1: DEMOSTRACIÓN CON UNA LISTA INICIAL
# ===================================================================

# Paso 1: Inicializar una lista vacía por defecto
libros = []
print("Paso 1: Incicializar una lista vacía.")
print(libros)

# Paso 2: Agregar 5 libros a la lista
libros = [
    ["El Aleph", 1949, 15.50],
    ["Cien años de soledad", 1967, 22.00],
    ["La sombra del viento", 2001, 18.75],
    ["Ficciones", 1944, 16.00],
    ["El túnel", 1948, 12.50]
]
print("Paso 2: Lista de libros actualizada con 5 títulos.")
print("Inventario inicial:", libros)
print("-" * 80)

# Paso 3: Use slicing para mostrar los primeros 3 libros
primeros_tres = libros[:3]
print("\nPaso 3: Mostrando los primeros 3 libros con slicing.")
print(primeros_tres)
print("-" * 80)

# Paso 4: Modifique el precio del segundo libro
print(f"\nPaso 4: Modificando el precio del segundo libro: '{libros[1][0]}'.")
print(f"Precio original: ${libros[1][2]}")
libros[1][2] = 25.50
print(f"Nuevo precio: ${libros[1][2]}")
print("-" * 80)

# Paso 5: Ordene los libros por año (ascendente y descendente)
libros_ascendente = sorted(libros, key=lambda libro: libro[1])
print("\nPaso 5: Libros ordenados por año (ascendente).")
print(libros_ascendente)
print("-" * 80)

# Paso 6: Filtre los libros con precio mayor a 20
print("\nPaso 6: Filtrando libros con precio mayor a $20.")
libros_caros_comp = [libro for libro in libros if libro[2] > 20]
print("Libros caros:", libros_caros_comp)
print("-" * 80)

# Paso 7: Elimine el último libro con pop y muestre el eliminado
print("\nPaso 7: Eliminando el último libro del inventario.")
libro_eliminado = libros.pop()
print(f"Libro eliminado: {libro_eliminado}")
print("-" * 80)

# Paso 8: Use enumerate para listar los libros actuales
print("\nPaso 8: Listado del inventario antes de la adición de nuevos libros.")
for indice, libro in enumerate(libros):
    print(f"Índice {indice}: Título: {libro[0]}, Año: {libro[1]}, Precio: ${libro[2]}")

# ===================================================================
# PARTE 2: MÓDULO INTERACTIVO PARA AÑADIR MÁS LIBROS
# ===================================================================

# Paso 9: Bucle para que el usuario agregue libros a la lista existente
print("\n" + "="*50)
print("Paso 9: Módulo para añadir nuevos libros al inventario existente.")
print("Cuando quieras terminar, simplemente escribe 'salir' en el título del libro.")
print("="*80)

libros_agregados = 0
while True:
    titulo = input("\nIntroduce el título del nuevo libro (o 'salir' para terminar): ")
    
    if titulo.lower() == 'salir':
        break
        
    try:
        anio = int(input("Introduce el año de publicación: "))
        precio = float(input("Introduce el precio (ej. 19.99): "))
        
        libros.append([titulo, anio, precio])
        libros_agregados += 1 # Aumentamos el contador de libros nuevos
        print(f"✔️ ¡Libro '{titulo}' agregado correctamente!")
        
    except ValueError:
        print("❌ Error: El año debe ser un número entero y el precio un número. Intenta de nuevo.")

# Paso 10: Mostrar el inventario final completo
print("\n" + "="*80)
print("✅ Paso 10: Sesión de adición finalizada.")

if libros_agregados > 0:
    print(f"Se agregaron {libros_agregados} libro(s) nuevo(s).")
else:
    print("No se agregaron libros nuevos.")

print("\n📊 INVENTARIO FINAL COMPLETO:")
for indice, libro in enumerate(libros):
    print(f"Índice {indice}: Título: {libro[0]}, Año: {libro[1]}, Precio: ${libro[2]}")
