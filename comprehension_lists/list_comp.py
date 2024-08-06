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
