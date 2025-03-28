def selection_sort(lista):
    for i in range(len(lista)):
        menor_indice = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    
    return lista

lista = [64, 25, 12, 22, 11]
print("Lista original:", lista)

lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)