import random

# Sistema de turnos para consultorio con tuplas
# 1. Inicializar tupla vacía para pacientes
pacientes = ()
print(f"1. La cola de pacientes inicia vacía: {pacientes}\n")

# 2. Agregar pacientes (nombres) a la cola
print("2. Llegan los primeros pacientes...")
pacientes = pacientes + ("Ana García", "Luis Martínez", "Eva Robles")
pacientes = pacientes + ("Ana García", "Carlos Soto") #Agregamos más, incluyendo un duplicado
print(f"   Cola actual: {pacientes}\n")

# 3. Simular atención removiendo el primer paciente
print("3. Atendiendo al siguiente paciente...")
if pacientes: # Nos aseguramos de que la cola no esté vacía
    paciente_atendido = pacientes[0]
    pacientes = pacientes[1:]
    print(f"Salió de la cola: '{paciente_atendido}'")
    print(f"Cola restante: {pacientes}\n")
else:
    print("No hay pacientes en la cola.\n")

# 4. Insertar una emergencia (paciente al inicio de la cola)
print("4. ¡Llega una emergencia!")
paciente_emergencia = "Omar Vega"
pacientes = (paciente_emergencia,) + pacientes
print(f"Cola con emergencia al frente: {pacientes}\n")

# 5. Generar lista de espera (copia de la cola actual)
lista_espera = pacientes[:]
print(f"5. Se genera una lista de espera (copia): {lista_espera}\n")

# 6. Usar count para ver cuántas veces aparece un nombre
nombre_buscar = "Ana García"
conteo = pacientes.count(nombre_buscar)
print(f"6. El nombre '{nombre_buscar}' aparece {conteo} veces en la cola.\n")

# 7. 'Barajar' la cola (creando nueva tupla ordenada aleatoriamente)
print("7. Se reorganiza la cola de forma aleatoria...")
# Para barajar, convertimos la tupla a una lista, reordenamos y reconvertimos a tupla.
lista_temporal = list(pacientes)
random.shuffle(lista_temporal)
pacientes_barajados = tuple(lista_temporal)
print(f"Cola original:  {pacientes}")
print(f"Cola barajada: {pacientes_barajados}\n")

# 8. Desempaquetar los primeros 3 pacientes en variables
print("8. Asignando los 3 primeros turnos a consultorios...")
if len(pacientes_barajados) >= 3:
    primero, segundo, tercero, *resto_cola = pacientes_barajados
    print(f"- Consultorio 1: {primero}")
    print(f"- Consultorio 2: {segundo}")
    print(f"- Consultorio 3: {tercero}")
    print(f"- Quedan en espera: {resto_cola}\n")
else:
    print("No hay suficientes pacientes para asignar los 3 turnos.\n")

# 9. Información adicional de la cola
print("9. Reporte final de la cola:")
print(f"- Número total de pacientes en la cola original: {len(pacientes)}")
paciente_a_verificar = "Eva Robles"
if paciente_a_verificar in pacientes:
    print(f"- '{paciente_a_verificar}' SÍ se encuentra en la cola.")
else:
    print(f"- '{paciente_a_verificar}' NO se encuentra en la cola.")