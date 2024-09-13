print("Ejemplo de tuplas")
canciones=("el triste","el carro rojo","Amor eterno")
print(canciones)
x = ("apple", "banana", "cherry")
y = list(canciones)
print(y)
y[1] = "La loca de san blas"
x = tuple(y)
print(x)
print("Listado de elementos de la tupla canciones con ciclo for")
for Garza in canciones:
    print(Garza)
