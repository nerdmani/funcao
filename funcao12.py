def ordenar_lista(lista):
    for i in range (len(lista)):
        for j in range(i + i, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista 
    
lista = [5, 2, 9, 1, 7]
print('A lista ordenada é: ', ordenar_lista(lista))