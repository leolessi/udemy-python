"""
Listas em Python, diferente das strings, são MUTÁVEIS.
Suportam diversos valores de qualquer tipo
Acesso por meio de índices e fatiamentos
Métodos úteis: append, insert, pop, del, clear, extend, +
    .append - Adiciona um item no final. Pode ser qualquer tipo aceito na lista. -> lista.append (item/'Item'/True/)
    .insert - Adiciona um item no indice escolhido. -> lista.insert(indice, valor)
    .pop - Remove do final ou do indice escolhido. -> lista.pop(indice) ou lista.pop() para remover o ultimo indice
    .del - Apaga um indice -> del lista[2]
    .clear - Limpa a lista -> lista.clear()
    .extend - Estende a lista -> listaA.extend(listaB)
    + -> Concatena a lista
"""

#        0      1          2           3               4
#       -5     -4         -3          -2              -1
# lista = [123, True, "Leonardo Lessi", 1.2, ["Nome1", "Nome2", "Nome3"]]

lista_A = [1, 2, 3]
lista_B = [4, 5, 6]
lista_AB = lista_A + lista_B
print("lista_AB = lista_A + lista_B -> ", lista_AB)

lista_A.extend(lista_B)
print("lista_A.extend(lista_B) -> ", lista_A)
