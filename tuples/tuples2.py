# Ejercicio 2: Números Complejos
# Descripción:
# Usa tuplas para representar números complejos y escribe funciones para sumarlos, restarlos y multiplicarlos.

# Instrucciones:

# Representa un número complejo como una tupla (a, b), donde a es la parte real y b es la parte imaginaria.
# Define funciones para sumar, restar y multiplicar dos números complejos.
# Ejemplo:



def suma_compleja(r, i):
    c2 = (r, i)
    real = c1[0] + c2[0]
    imaginaria = c1[1] + c2[1]
    suma_comp = (real, imaginaria)
    return suma_comp

def resta_compleja(r, i):
    c2 = (r, i)
    real = c1[0] - c2[0]
    imaginaria = c1[1] - c2[1]
    resta_comp = (real, imaginaria)
    return resta_comp

def multiplica_compleja(r, i):
    c2 = (r, i)
    real = c1[0] * c2[0]
    imaginaria = c1[1] * c2[1]
    multiplica_comp = (real, imaginaria)
    return multiplica_comp

while True:
    try:
        c1 = (1, 2)
        c2a = int(input("Ingrese parte real del número: "))
        c2b = int(input("Ingrese parte imaginaria del número: "))

        print(suma_compleja(c2a, c2b))
        print(resta_compleja(c2a, c2b))
        print(multiplica_compleja(c2a, c2b))
    except KeyboardInterrupt:
        break
    except ValueError as e:
        print(f"Error: {e}")
        continue
    except:
        break