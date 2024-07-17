# Ejercicio 3: Inventario de Tienda
# Descripción:
# Escribe un programa para gestionar el inventario de una tienda. El programa debe permitir agregar nuevos productos, actualizar la cantidad de productos existentes, y eliminar productos del inventario.

# Instrucciones:

# Crea un diccionario donde las claves sean los nombres de los productos y los valores sean la cantidad disponible.
# Implementa funciones para agregar, actualizar y eliminar productos del inventario.
# Implementa una función para mostrar el inventario actual.
# Ejemplo:

# python
# Copiar código
# inventory = {
#     "manzanas": 50,
#     "naranjas": 30,
#     "plátanos": 20
# }

# # Función para agregar un producto
# # Función para actualizar la cantidad de un producto
# # Función para eliminar un producto
# # Función para mostrar el inventario

# # Resultado esperado después de varias operaciones:
# inventory = {
#     "manzanas": 45,
#     "naranjas": 40,
#     "plátanos": 0,
#     "uvas": 25
# }

inventory = {}

while True:
    try:
        def agregar_prod():
            producto = input("Nombre del producto: ").lower()
            if producto in inventory:
                print(f"{producto.capitalize()} already exists in inventory")
                actualizar_cant_prod()
            else:
                cantidad_prod = int(input("Ingrese cantidad del producto: "))
                inventory.update({producto: cantidad_prod})
            mostrar_inventario()


        def actualizar_cant_prod():
            producto = input("Nombre del producto: ").lower()
            if producto in inventory:
                while True:
                    try:
                        action = input("Agregar=1, Quitar=2. Desea agregar o quitar productos? ")
                        cantidad_prod = int(input("Ingrese cantidad del producto: "))
                        if action == "1" or action == "agregar":
                            inventory[producto] += cantidad_prod
                        else:
                            negativo = inventory[producto] - cantidad_prod
                            if negativo < 0:
                                print("Está intentando eliminar más unidades de las que existen en el inventario!")
                            else:
                                inventory[producto] -= cantidad_prod
                        mostrar_inventario()
                    except ValueError as e:
                        print(f"Ingreso inválido. Error: {e}")
                        continue
                    except TypeError as e:
                        print(f"Ingreso inválido. Error: {e}")
                        continue
                    except KeyboardInterrupt as e:
                        print("Se interrumpió la ejecución del programa")
                        break
                    except:
                        print("Un error inesperado ha ocurrido")
                        break
            else:
                return print(f"{producto.capitalize()} does not exist in the current inventory") 
            mostrar_inventario()


        def eliminar_prod():
            producto = input("Nombre del producto: ").lower()
            if producto in inventory:
                del inventory[producto]
                print(f"{producto.capitalize()} was successfully deleted")
                mostrar_inventario()
            else:
                print("Product does not exist in the current inventory")


        def mostrar_inventario():
            order_keys = sorted(inventory.keys())
            inventory_in_order = {}
            for k in order_keys:
                inventory_in_order[k] = inventory[k]
            print(inventory_in_order)

        def consultar():
            ingreso = input("Agregar=1, Actualizar cant=2, Eliminar=3, Ver inventario=cualquier tecla. Ingrese un valor: ")
            if ingreso == "1" or ingreso == "agregar":
                agregar_prod()
            elif ingreso == "2" or ingreso == "actualizar":
                actualizar_cant_prod()
            elif ingreso == "3" or ingreso == "eliminar":
                eliminar_prod()
            else:
                mostrar_inventario()

        consultar()
    
    except ValueError as e:
        print(f"Ingreso inválido. Error: {e}")
        continue
    except TypeError as e:
        print(f"Ingreso inválido. Error: {e}")
        continue
    except KeyboardInterrupt as e:
        print("Se interrumpió la ejecución del programa")
        break
    except:
        print("Un error inesperado ha ocurrido")
        break

