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

elif choise == 3:
    # Dado un número flag_register, escribe un código para alternar el cuarto bit (contando desde 0).
    flag_register = 0b11001100
    mask = 2 ** 4

    print("Binary flag_register before mask:", bin(flag_register))
    print("Mask:", bin(mask))

    flag_register = flag_register ^ mask

    print("Binary flag_register before mask:", bin(flag_register))
    print("flag_register after mask:", flag_register)

elif choise == 4:
    # Dado un número flag_register, escribe un código para verificar si el tercer bit (contando desde 0) está establecido en 1. Si está en 1, cambia el estado del tercer bit a 0; si está en 0, cambia el estado del tercer bit a 1.
    flag_register = 0b1111111
    mask = 2 ** 3
    print("flag_register before change:", bin(flag_register))
    result = flag_register & mask
    print("result:", bin(result))
    
    if result == 0b1000:
        flag_register = flag_register & ~mask
        print("flag_register & ~mask:", bin(flag_register))
    else:
        flag_register = flag_register | mask
        print("flag_register | mask:", bin(flag_register))

elif choise == 5:
    # Dado un número flag_register, escribe un código para verificar si el segundo bit (contando desde 0) está establecido en 0. Si está en 0, establece el segundo bit a 1.
    flag_register = 0b0011000
    mask = 2 ** 2
    print("flag_register:", bin(flag_register))
    print("mask:", bin(mask))
    
    if not (flag_register & mask):
        flag_register = flag_register | mask
        print("flag register post conditional, second bit is now changed to zero:", bin(flag_register))
    else:
        print("flag_register's second bit is 1")