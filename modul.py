def zmien(a):
    a = 8
    return a


a = 7
#Jest przekazywana kopia argumentu
zmien (a)
print(a)

def zmien_liste(lista):
    lista.append("HAHA!")
    return lista
lista = [1, 2]
