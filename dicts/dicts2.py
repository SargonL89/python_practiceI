# Ejercicio 2: Diccionario de Notas
# Descripción:
# Escribe un programa que permita al usuario ingresar los nombres de estudiantes y sus respectivas calificaciones en varias materias. Luego, el programa debe calcular y mostrar el promedio de cada estudiante.

# Instrucciones:

# Crea un diccionario donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario con las materias y sus respectivas calificaciones.
# Calcula el promedio de calificaciones de cada estudiante y almacénalo en otro diccionario.
# Ejemplo:

# students = {
#     "Ana": {"Matemáticas": 90, "Ciencia": 85, "Literatura": 88},
#     "Luis": {"Matemáticas": 75, "Ciencia": 80, "Literatura": 72},
#     "Marta": {"Matemáticas": 85, "Ciencia": 89, "Literatura": 90}
# }

# # Resultado esperado:
# averages = {
#     "Ana": 87.67,
#     "Luis": 75.67,
#     "Marta": 88.0
# }

students = {}
averages = {}

while True:
    try: 
        def dict_of_students(stud, mater, qualif):
            if stud in students:
                if mater in students[stud]:
                    students[stud][mater] = qualif
                else:
                    students[stud][mater] = ""
                    students[stud][mater] = qualif
            else:
                students[stud] = {}
                students[stud][mater] = qualif
            
            return students_average(students, stud)
        
        def students_average(dicc, stud):
            ave = 0
            num_mater = 0
            for i in dicc[stud]:
                ave += dicc[stud][i]
                num_mater += 1
            ave = format(ave / num_mater, ".2f")
            if stud in averages:
                averages[stud] = ave
            else:
                averages.update({stud: ave})
            
            return averages

        estudiante = input("Estudiante: ").title()
        materia = input("Materia: ").title()
        calificacion = int(input("Calificación: "))

        print(dict_of_students(estudiante, materia, calificacion))
    
    except TypeError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        break
    except:
        continue