"""
Exiba os indices da lista
0 Maria
1 Helena
2 Leonardo
"""

# declara a lista
lista = ["Maria", "Helena", "Leonardo"]

# pega o range da lista
total_indices_lista = range(len(lista))

# percorre todos os indices e printa o indice + o elemento[i] da lista
for indice in total_indices_lista:
    print(indice, lista[indice])
