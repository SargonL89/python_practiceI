# Ejercicio 1: Intercambio de Valores
# Descripción:
# Escribe una función que tome dos variables y las intercambie usando tuplas.

# Instrucciones:

# Define una función que tome dos argumentos.
# Usa una tupla para intercambiar los valores de los dos argumentos.
# Devuelve los valores intercambiados.
# Ejemplo:


def swap(a, b):
    tup_1 = (a, b)
    tup_2 = (tup_1[1], tup_1[0])
    return tup_2


x = int(input("Primer ingreso: "))
y = int(input("Segundo ingreso: "))
x, y = swap(x, y)
print(x, y)