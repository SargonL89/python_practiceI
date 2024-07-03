# Descripción: Escribe un programa que imprima todos los números pares entre 10 y 50 (inclusive).

# for i in range(10, 51):
#     if i % 2 == 0:
#         print(i)

# Descripción: Escribe una función que reciba dos números enteros, a y b, y devuelva la suma de todos los múltiplos de 3 que se encuentran entre a y b (exclusivo).

def sum_mult3(a, b):
    suma = 0
    for i in range(a, b):
        if i % 3 == 0:
            suma += i
    return suma

print(sum_mult3(3, 40))

# Descripción: Escribe un programa que imprima la tabla de multiplicar del 5 desde el 1 hasta el 10. La salida debe ser algo como:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

