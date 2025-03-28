lista = [7,5,1,8,3]
n = len (lista)
minimo = lista [0]
for i in range (n)
    if lista [i] < minimo:
        minimo = lista[1]
print(minimo)

#como achar o numero

lista = [7,5,1,8,3]
def selection_sort (lista):
    n = len (lista)
    min_index = 0
    for i in range (n):
        if lista[1]<lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista [min_index] = aux