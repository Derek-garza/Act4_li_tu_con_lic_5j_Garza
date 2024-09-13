print("Ejemplo de tuplas")
canciones=("Te amo","El NoaNoa","Amor eterno")
print(canciones)
x = ("apple", "banana", "cherry")
y = list(canciones)
print(y)
y[1] = "La puerta negra"
x = tuple(y)
print(x)
print("Listado de elementos de la tupla canciones con ciclo for")
for Garcia in canciones:
    print(Garcia)