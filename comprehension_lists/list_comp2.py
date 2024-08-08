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