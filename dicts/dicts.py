# Ejercicio 1: Contador de Palabras
# Descripción:
# Escribe una función que tome una cadena de texto y devuelva un diccionario donde las claves sean las palabras y los valores sean el número de veces que cada palabra aparece en la cadena.

# Instrucciones:

# La función debe ignorar mayúsculas y minúsculas (es decir, "Python" y "python" deben considerarse la misma palabra).
# Ignora signos de puntuación.
# Ejemplo:
# input_str = "Hola, cómo estás? Hola, estoy bien. Y tú?"
# output = {
#     "hola": 2,
#     "cómo": 1,
#     "estás": 1,
#     "estoy": 1,
#     "bien": 1,
#     "y": 1,
#     "tú": 1
# }

# dicc = {}

# def text_to_dict(string):
#     string = string.lower()
#     word = ""
#     for letter in string:
#         if not letter.isalpha():
#             word = word.strip()
#             if word == "":
#                 continue
#             elif word in dicc:
#                 dicc[word] += 1
#             else:
#                 dicc.update({word: 1})
#             word = ""
#         else:
#             word += letter
#     print(dicc)

# intro = input("Redacta algo: ")
# text_to_dict(intro)

dicc2 = {}

def text_to_dict2(string):
    string = string.lower().split()
    for word in string:
        palabra = ""
        for letter in word:
            if letter.isalpha():
                palabra += letter
            else:
                continue
        if palabra in dicc2:
            dicc2[palabra] += 1
            continue
        else:
            dicc2.update({palabra: 1})
    print(dicc2)

intro2 = input("Redacta algo: ")
text_to_dict2(intro2)