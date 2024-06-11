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