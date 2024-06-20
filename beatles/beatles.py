# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("George Harrison")
beatles.append("Paul McCartney")
print("Paso 2:", beatles)

# paso 3
for _ in range(2):
    new = input("Agrega un nuevo beatle: ")
    beatles.append(new)
print("Paso 3:", beatles)

# paso 4
print("Paso 4:", beatles)
del beatles[0]
del beatles[0]


# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))

