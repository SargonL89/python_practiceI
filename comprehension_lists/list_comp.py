import random

# Ejercicio 1: Números Pares
# Descripción:
# Crea una lista que contenga los números pares del 1 al 20 usando comprensión de listas.
# Instrucciones:
# Utiliza una comprensión de listas para generar los números pares del 1 al 20.

pares = [x for x in range(21) if x % 2 == 0]
print(pares)


# Ejercicio 2: Cuadrados de Números
# Descripción:
# Crea una lista que contenga los cuadrados de los números del 1 al 10 usando comprensión de listas.
# Instrucciones:
# Utiliza una comprensión de listas para generar los cuadrados de los números del 1 al 10.

cuadrados = [x ** 2 for x in range(11)]
print(cuadrados)


# Ejercicio 3: Filtrar Palabras
# Descripción:
# Dada una lista de palabras, crea una nueva lista que contenga solo las palabras que tienen más de 3 letras usando comprensión de listas.
# Instrucciones:
# Define una lista de palabras.
# Utiliza una comprensión de listas para filtrar las palabras que tienen más de 3 letras.

lista_completa = ["alf", "manzana", "arbol", "casa", "gol", "po", "esc", "persona", "tigre"]
lista_de_3 = [palabra for palabra in lista_completa if len(palabra) <= 3]
print(lista_de_3)


# Ejercicio 4: Convertir Lista de Listas
# Descripción:
# Dada una lista de listas que contiene números, crea una nueva lista que contenga la suma de los números en cada sublista usando comprensión de listas.
# Instrucciones:
# Define una lista de listas, donde cada sublista contiene varios números.
# Utiliza una comprensión de listas para crear una nueva lista que contenga la suma de los números en cada sublista.


listas_random = [[x for x in random.sample(range(10, 40), random.randrange(1, 12))] for i in range(3)]
print(listas_random)
listas_sumadas = [sum([i for i in x]) for x in listas_random]
print(listas_sumadas)