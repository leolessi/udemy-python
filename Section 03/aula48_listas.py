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

"""
Cuidados com dados mutaveis

    Com dados imutaveis (strings), o = copia o valor
        stringA = "Leonardo"
        stringB = stringA
        stringA = "Leonardo Lessi"
    Nesse caso, a stringA muda seu valor para 'Leonardo Lessi' e a stringB continua com o valor 'Leonardo'

    Com dados mutaveis (listas), o = aponta para o mesmo valor na memoria
        listaA = ['Leonardo', 'Maria']
        listaB = listaA

        listaA[1] = 'Mutavel'
    Nesse caso, a listaA e a listaB retornam o mesmo valor na memoria -> ['Leonardo', 'Mutavel']
    Para contornar essa situacao, utilizamos o metodo .copy:
        listaA = ['Leonardo', 'Maria']
        listaB = listaA.copy()

        listaA[1] = 'Mutavel'
    Ja nesse caso, a listaB retorna o valor inicial da listaA (['Leonardo', 'Maria']) e a listaA retorna o valor modificado (['Leonardo', 'Mutavel'])
"""

"""
For in com listas
"""

lista = ["Maria", "Helena", "Leonardo"]

for nome in lista:
    print(nome)

# for i, nome in enumerate(lista):
#     if i == 1:
#         print(nome)
