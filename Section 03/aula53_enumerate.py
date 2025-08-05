"""
enumerate = enumera iteraveis (indices)
"""

lista = "Leonardo", "Maria", "Helena"
# lista = ["Leonardo", "Maria", "Helena"]


for indice, nome in enumerate(lista):
    # if indice % 2 == 0:
    # print(indice, nome, lista[indice])
    print(indice, nome)


# basicamente, faz o descrito abaixo
# for tupla_enumerada in enumerate(lista):
#     for valor in tupla_enumerada:
#         print(f"\t{valor}")
