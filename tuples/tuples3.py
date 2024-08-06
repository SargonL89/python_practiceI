# Ejercicio 3: Análisis de Datos de Temperatura
# Descripción:
# Dado un registro de temperaturas diarias representado por una lista de tuplas, donde cada tupla contiene el día del mes y la temperatura máxima y mínima del día, escribe un programa que calcule la temperatura promedio de todo el mes.

# Instrucciones:

# Crea una lista de tuplas donde cada tupla sea (día, temperatura_máxima, temperatura_mínima).
# Calcula la temperatura promedio del mes.
# Encuentra el día con la mayor diferencia entre la temperatura máxima y mínima.
# Ejemplo:

registros = [
    (1, 30, 15),
    (2, 32, 18),
    (3, 28, 14),
    (4, 25, 8),
    (5, 22, 2),
    (6, 12, -3),
    (7, 8, -5),
]

def temperatura_promedio(registros):
    n = 0
    suma_prom = 0
    for _ in registros:
        prom = (registros[n][1] + registros[n][2]) / 2
        suma_prom += prom
        n += 1
    temp_prom = suma_prom / n
    print(f"La tmperatura promedio de la semana fue de: {round(temp_prom, 2)}°")


def mayor_diferencia(registros):
    n = 0
    max_dif = 0
    for _ in registros:
        resta = abs(registros[n][1] - registros[n][2])
        if resta > max_dif:
            max_dif = resta
            dia = registros[n][0]
        n += 1
    print(f"La mayor diferencia intradiaria entre temperaturas máxima y mínima se dio el dia {dia}, con una diferencia de {max_dif}°")


temperatura_promedio(registros)
mayor_diferencia(registros)