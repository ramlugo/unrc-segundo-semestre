# Procesamiento de datos climáticos con tuplas
# 1. Crear tupla con temperaturas de una semana
temperaturas_semana = (25, 28, 30, 27, 26, 29, 31)
print(f"1. Temperaturas de la semana (Celsius): {temperaturas_semana}\n")

# 2. Calcular el promedio (usando sum y len)
promedio = sum(temperaturas_semana) / len(temperaturas_semana)
# Usamos f-string para formatear el resultado a 2 decimales
print(f"2. Temperatura promedio: {promedio:.2f}°C\n")

# 3. Encontrar temperatura máxima y mínima
temp_max = max(temperaturas_semana)
temp_min = min(temperaturas_semana)
print(f"3. Temperatura máxima: {temp_max}°C")
print(f"Temperatura mínima: {temp_min}°C\n")

# 4. Crear tupla con temperaturas en Fahrenheit (usando generator expression)
# Fórmula: F = C * 9/5 + 32
temps_fahrenheit = tuple((c * 9/5) + 32 for c in temperaturas_semana)
print("4. Temperaturas en Fahrenheit:")
# Usamos otro generator para imprimir los valores formateados
print(tuple(f"{f:.2f}°F" for f in temps_fahrenheit))
print("-" * 40)

# 5. Modificar un rango de temperaturas (días 2 al 4) - creando nueva tupla
print("5. Modificando las temperaturas de los días 2, 3 y 4...")
nuevas_temps_centrales = (29, 32, 30) # Nuevos valores para esos días
# Reconstruimos la tupla completa
temperaturas_modificadas = temperaturas_semana[:1] + nuevas_temps_centrales + temperaturas_semana[4:]
print("Tupla original:   ", temperaturas_semana)
print("Tupla modificada: ", temperaturas_modificadas)
print("-" * 40)

# 6. Añadir nuevas temperaturas (creando nuevas tuplas)
print("6. Añadiendo las temperaturas de los siguientes dos días...")
temps_adicionales = (33, 24)
semana_extendida = temperaturas_modificadas + temps_adicionales
print("Semana con días adicionales:", semana_extendida)
print("-" * 40)

# 7. Dividir la tupla en dos partes usando slicing
print("7. Dividiendo la tupla original en dos mitades...")
# El punto de división puede ser el que necesitemos. Aquí la partimos en 4 y 3.
primera_parte = temperaturas_semana[:4]
segunda_parte = temperaturas_semana[4:]
print("Primera parte:", primera_parte)
print("Segunda parte:", segunda_parte)
print("-" * 40)

# 8. Filtrar temperaturas (creando nueva tupla sin valores bajos)
print("8. Filtrando para mantener solo temperaturas superiores a 27°C...")
umbral = 27
temps_altas = tuple(temp for temp in temperaturas_semana if temp > umbral)
print(f"Temperaturas originales: {temperaturas_semana}")
print(f"Temperaturas filtradas (> {umbral}°C): {temps_altas}")