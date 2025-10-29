"""
Soluciones de ejercicios de programación para la asignatura 
Programación para la Ciencia de Datos de la Licenciatura en 
Ciencia de Datos para Negocios (Semestre 2025-2).
"""

# --- Problema 1: Suma de Elementos en una Lista ---

def sumar_elementos_lista(lista_numeros):
    """
    Calcula la suma de todos los elementos en una lista de números.

    Esta función itera manualmente sobre la lista usando un ciclo 'for'
    Parámetros:
    lista_numeros (list): Una lista de números enteros.

    Retorna:
    int: La suma total de los elementos. Retorna 0 si la lista está vacía.
    """
    # Inicializamos una variable 'acumulador' para guardar la suma
    suma_total = 0
    
    # Iteramos sobre cada 'elemento' en la 'lista_numeros'
    for elemento in lista_numeros:
        # Acumulamos el valor del elemento actual en 'suma_total'
        suma_total += elemento # Equivalente a: suma_total = suma_total + elemento
    
    # Retornamos el resultado final
    return suma_total

# --- Problema 2: Generación de Números Pares en un Rango ---

def generar_numeros_pares(limite_superior):
    """
    Genera una lista de números pares desde 1 hasta un límite dado.

    Utiliza una 'list comprehension'. Esta es una forma avanzada, 
    eficiente y Pythonica de crear listas, que internamente utiliza 
    un ciclo 'for'.

    Parámetros:
    limite_superior (int): El número máximo (inclusivo) del rango.

    Retorna:
    list: Una lista de números pares.
    """
    
    # Usamos range(start, stop, step)
    # start = 2 (el primer número par en el rango 1-50)
    # stop = limite_superior + 1 (para que range() incluya el 50)
    # step = 2 (para saltar de par en par)
    
    lista_pares = [num for num in range(2, limite_superior + 1, 2)]
    
    return lista_pares

# --- Problema 3: Contar Estudiantes Aprobados en un Diccionario ---

def analizar_calificaciones(dict_calificaciones, min_aprobatoria=60):
    """
    Analiza un diccionario de calificaciones para clasificar a los
    estudiantes en aprobados y reprobados.

    Itera sobre un diccionario usando el método .items() para obtener 
    clave (estudiante) y valor (calificación).
    Devuelve un 'reporte' estructurado (un diccionario), lo cual es más 
    útil y mantenible que variables sueltas.

    Parámetros:
    dict_calificaciones (dict): Diccionario {nombre: calificación}
    min_aprobatoria (int): Calificación mínima para aprobar. Default 60.

    Retorna:
    dict: Un diccionario con el conteo y las listas de aprobados/reprobados.
    """
    # Inicializamos listas vacías para almacenar los nombres
    lista_aprobados = []
    lista_reprobados = []
    
    # Iteramos sobre el diccionario. .items() nos da acceso
    # tanto a la clave (estudiante) como al valor (calificacion)
    for estudiante, calificacion in dict_calificaciones.items():
        if calificacion >= min_aprobatoria:
            lista_aprobados.append(estudiante)
        else:
            lista_reprobados.append(estudiante)
            
    # Creamos el reporte estructurado
    reporte = {
        'conteo_aprobados': len(lista_aprobados),
        'conteo_reprobados': len(lista_reprobados),
        'lista_aprobados': lista_aprobados,
        'lista_reprobados': lista_reprobados
    }
    
    return reporte

# --- Bloque Principal de Ejecución ---

# Usar __name__ == "__main__" es una 'best practice' en Python.
# Le dice al script que solo ejecute este bloque si se corre
# directamente (y no si es importado por otro script).
if __name__ == "__main__":
    
    print("--- Soluciones de Ejercicios de Programación ---")
    
    # --- Ejecución Problema 1 ---
    lista_entrada_p1 = [10, 25, 5, 30, 50, 15]
    resultado_p1 = sumar_elementos_lista(lista_entrada_p1)
    print(f"\n Problema 1: Suma de Elementos en una Lista")
    print(f"   Lista de entrada: {lista_entrada_p1}")
    print(f"   Resultado (Suma): {resultado_p1}")

    # --- Ejecución Problema 2 ---
    limite_p2 = 50
    resultado_p2 = generar_numeros_pares(limite_p2)
    print(f"\n Problema 2: Generación de Números Pares (1 a {limite_p2})")
    print(f"   Lista de Pares: {resultado_p2}")

    # --- Ejecución Problema 3 ---
    calificaciones_curso = {
        'Ramses Lugo': 92,
        'Isi Cruz': 99,
        'Leslie Alvarado': 76,
        'Manuel Palma': 81,
        'Damián Sánchez': 60,
        'Leo Dan': 45
    }
    reporte_p3 = analizar_calificaciones(calificaciones_curso)
    
    print(f"\n Problema 3: Contar Estudiantes Aprobados")
    print(f"   Datos de entrada: {calificaciones_curso}")
    print(f"   Total Aprobados: {reporte_p3['conteo_aprobados']}")
    print(f"   Total Reprobados: {reporte_p3['conteo_reprobados']}")
    print(f"   Lista Aprobados: {reporte_p3['lista_aprobados']}")
    print(f"   Lista Reprobados: {reporte_p3['lista_reprobados']}")