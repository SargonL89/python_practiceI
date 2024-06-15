eleccion_programa = int(input("Elija una opción: "))

if eleccion_programa == 1:
    # Conversor de unidades

    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = (miles * 1.61) / 1
    kilometers_to_miles = (kilometers * 1) / 1.61

    print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
    print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

    dollars = 3000
    pesos_ars = 900000

    pesos_to_dollars = (pesos_ars * 1) / 1200
    dollars_to_pesos = (dollars * 1200) / 1

    print(pesos_ars, "pesos son", round(pesos_to_dollars, 1), "dólares")
    print(dollars, "dólares son", round(dollars_to_pesos, 1), "pesos")

elif eleccion_programa == 2:
    # Evaluar valor de y

    x =  0
    x = float(x)
    y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
    print("y =", y)

    x =  1
    x = float(x)
    y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
    print("y =", y)

    x =  -1
    x = float(x)
    y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
    print("y =", y)

elif eleccion_programa == 3:
    # Operadores y expresiones

    hour = int(input("Hora de inicio (horas): "))
    mins = int(input("Minuto de inicio (minutos): "))
    dura = int(input("Duración del evento (minutos): "))

    hours_to_mins = hour * 60
    total_mins = (hours_to_mins + mins) + dura

    event_total_mins = int(total_mins % 60)
    event_total_hours = total_mins - event_total_mins
    event_total_hours = int(event_total_hours / 60)

    event_total_hours = event_total_hours % 24

    print(f"Hora de finalización del evento: {event_total_hours}:{event_total_mins}")

elif eleccion_programa == 4:
    # Contador pares - impares

    # Un programa que lee una secuencia de números
    # y cuenta cuántos números son pares y cuántos son impares.
    # El programa termina cuando se ingresa un cero.
    
    odd_numbers = 0
    even_numbers = 0
    
    # Lee el primer número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
    
    # 0 termina la ejecución.
    while number != 0:
        # Verificar si el número es impar.
        if number % 2 == 1:
            # Incrementar el contador de números impares odd_numbers.
            odd_numbers += 1
        else:
            # Incrementar el contador de números pares even_numbers.
            even_numbers += 1
        # Leer el siguiente número.
        number = int(input("Introduce un número o escribe 0 para detener: "))
    
    # Imprimir resultados.
    print("Conteo de números impares:", odd_numbers)
    print("Conteo de números pares:", even_numbers)

elif eleccion_programa == 5:
    # Evaluador de Hipótesis de Collatz

    c0 = int(input("Elige un número natural (distinto de cero y positivo): "))
    steps = 0

    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
            print(c0)
        else:
            c0 = 3 * c0 + 1 
            print(c0)
        steps += 1
    
    print("Pasos: ", steps)

else:
    # File extensions

    file_name = input("File name: ").lower().strip()

    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpg"):
        print("image/jpeg")
    elif file_name.endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
