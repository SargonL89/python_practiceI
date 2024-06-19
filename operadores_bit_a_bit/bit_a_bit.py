choise = int(input("Elija una opción: "))

if choise == 1:
    # 1- Dado un número flag_register, escribe un código para verificar si el quinto bit (contando desde 0) está establecido en 1.
    flag_register = 0b10101010
    mask = 32

    if flag_register & mask:
        print("El quinto bit está establecido en 1")
        print(bin(flag_register))
    else:
        print("El quinto bit está establecido en 0")
        print(bin(flag_register))

elif choise == 2:
    # Dado un número flag_register, escribe un código para establecer el séptimo bit (contando desde 0) en 1.
    flag_register = 0b01010101
    mask = 2 ** 7

    print("flag_register original en binario:", bin(flag_register))
    print("flag_register original en decimal:", flag_register)

    flag_register = flag_register | mask 

    print("flag_register post-mask en binario:", bin(flag_register))
    print("flag_register post-mask en binario:", flag_register)