# INICIO
# Inicialización de variables.
a = ["Pedro", 555, "Python", "Intel", "HP"]
b = [45, -67.8, 999.99, -2702.2, 1858]
c = ["mouse", "teclado", "monitor", "gabinete"]

# Longitud de la lista a y b separadas lista.
print(f"La longitud de la lista a es: {len(a)} elementos")
print(f"La longitud de la lista b es: {len(b)} elementos")
print("-"*100)

# Máximo de la  lista b.
maximo_b = max(b)
print(f"El valor más alto de la lista b es: {maximo_b}")
print("-"*100)

# Mínimo de la lista c.
minimo_c = min(c, key=len)
print(f"El elemento más corto de la lista c es: {minimo_c}")
print("-"*100)

# Añadir un elemento a la lista c.
c.append("adaptador")
print(f"Se añadió el elemento {c[-1]} a la lista c")
print("-"*100)

# Extender la lista a con la lista c.
a.extend(c)
print("Se añadieron los elementos a la lista a")
print(a)
print("-"*100)

# Insertar 47 en la posición 2 de la lista b.
b.insert(1, 47)
print("Lista b actualizada:")
print(b)
print("-"*100)

# Extrae el elemento en la posición 3 de la lista b.
print(f"El tercer elemento de la lista b es: {b[2]}")
print("-"*100)

# Extrae el último elemento de la lista b.
print(f"El último elemento de la lista b es: {b[-1]}")
print("-"*100)

# Borra el elemento en el indice 0 de la lista b.
b.pop(0)
print("Lista b actualizada:")
print(b)
print("-"*100)

# Invierte el orden de los elementos de la lista a.
print(a)
print("Lista a invertida:")
print(a.reverse)
print("-"*100)

# Ordena  los elementos de la lista b.
b_asc = sorted(b, reverse=False)
print(b_asc)
b_des = sorted(b, reverse=True)
print(b_asc)
print("-"*100)

# Unir las variables en una sola
unidas = a+b+b
print("Listas unidas en una sola:")
print(unidas)

# FIN