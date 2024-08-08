import random

# Ejercicio 1: Longitud de las Palabras
# Usa comprensión de listas y la función len() para crear una lista que contenga las longitudes de las palabras en una lista de palabras.
palabras = ["Python", "es", "genial"]
# # Resultado esperado: [6, 2, 6]

lista_1 = [len(w) for w in palabras]
print("lista 1:", lista_1)


# Ejercicio 2: Máximo de una Lista de Listas
# Usa comprensión de listas y la función max() para encontrar el valor máximo de cada lista en una lista de listas.
list_lists_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Resultado esperado: [3, 6, 9]

lista_2 = [max(n) for n in list_lists_2]
print("lista 2:", lista_2)


# Ejercicio 3: Mínimo de una Lista de Listas
# Usa comprensión de listas y la función min() para encontrar el valor mínimo de cada lista en una lista de listas.
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Resultado esperado: [1, 4, 7]

lista_3 = [min(n) for n in list_lists_2]
print("lista 3:", lista_3)


# Ejercicio 4: Redondear Números
# Usa comprensión de listas y la función round() para redondear una lista de números flotantes a dos decimales.
# round() redondea el valor al número entero más cercano
list_float_numbers = [3.14159, 2.71828, 1.61803]
# # Resultado esperado: [3.14, 2.72, 1.62]

lista_4 = [round(n) for n in list_float_numbers]
print("lista 4:", lista_4)


# Ejercicio 5: Generar Rango de Números
# Usa comprensión de listas y la función range() para crear una lista de los primeros 10 números pares.
# # Resultado esperado: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

lista_5 = [n for n in range(20) if n % 2 == 0]
print("lista 5:", lista_5)


# Ejercicio 6: Suma de Listas
# Usa comprensión de listas y la función sum() para sumar los elementos de cada lista en una lista de listas.
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Resultado esperado: [6, 15, 24]

lista_6 = [sum(n) for n in list_lists_2]
print("lista 6:", lista_6)


# Ejercicio 7: Potencia de Números
# Usa comprensión de listas y la función pow() para elevar cada número de una lista a la potencia de 2.
list_int_numbers = [1, 2, 3, 4, 5, 6, 7]
# # Resultado esperado: [1, 4, 9, 16, 25]

lista_7 = [pow(n, 2) for n in list_int_numbers]
print("lista 7:", lista_7)


# Ejercicio 8: Valor Absoluto de Números
# Usa comprensión de listas y la función abs() para obtener el valor absoluto de cada número en una lista.
numeros_8 = [-1, -2, -3, 4, 5]
# # Resultado esperado: [1, 2, 3, 4, 5]

lista_8 = [abs(x) for x in numeros_8]
print("lista 8:", lista_8)


# Ejercicio 9: Convertir a Conjunto
# Usa comprensión de listas y la función set() para crear un conjunto de los caracteres únicos en una cadena de texto.
texto = "abracadabra"
# # Resultado esperado: {'a', 'b', 'c', 'd', 'r'}

lista_9 = set([x for x in texto])
print("lista 9:", lista_9)


# Ejercicio 10: Ordenar Listas
# Usa comprensión de listas y la función sorted() para ordenar cada lista en una lista de listas.
listas_10 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
# # Resultado esperado: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lista_10 = [sorted(x) for x in listas_10]
print("lista 10:", lista_10)


# Ejercicio 11: Enumerar Elementos
# Usa comprensión de listas y la función enumerate() para crear una lista de tuplas que contengan el índice y el valor de cada elemento en una lista.
numeros_11 = [10, 20, 30]
# # Resultado esperado: [(0, 10), (1, 20), (2, 30)]

lista_11 = [x for x in enumerate(numeros_11)]
print("lista 11:", lista_11)


# Ejercicio 12: Filtrar Números Pares
# Usa comprensión de listas y la función filter() para crear una lista de los números pares en una lista de números.
numeros_12 = [x for x in random.sample(range(0, 50), random.randrange(10, 30))]
# # Resultado esperado: [2, 4, 6]

# Alternate: lista_12 = list(filter(lambda x: x % 2 == 0, numeros_12))
lista_12 = [x for x in filter(lambda x: x % 2 == 0, numeros_12)]
print("lista 12:", lista_12)


# Ejercicio 13: Mapear a Números Cuadrados
# Usa comprensión de listas y la función map() para crear una lista de los cuadrados de los números en una lista.
numeros_13 = [1, 2, 3, 4, 5]
# # Resultado esperado: [1, 4, 9, 16, 25]

# Alternate: lista_13 = list(map(lambda x: x ** 2, numeros_13))
lista_13 = [x for x in map(lambda x: x ** 2, numeros_13)]
print("lista 13:", lista_13)


# Ejercicio 14: Emparejar Listas
# Usa comprensión de listas y la función zip() para crear una lista de tuplas que emparejen elementos de dos listas.
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
# # Resultado esperado: [(1, 'a'), (2, 'b'), (3, 'c')]

lista_14 = [x for x in zip(numeros_12, lista2)]
print("lista 14:", lista_14)