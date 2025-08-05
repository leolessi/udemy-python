"""
Faca uma lista de compras.
1. O usuario deve poder:
    Inserir
    Apagar
    Listar
2. Nao permitir que o programa quebre com erros de indices inexistentes na lista
-> [i], [a], [l] (.upper)
-> validar apenas uma letra para escolher as opcoes / numeros para apagar os indices
"""

import os

opcoes_validas = "LAIS"
lista_de_compras = []

while True:
    escolha_usuario = input(
        "Escolha uma das opções: [i]nserir | [a]pagar | [l]istar | [s]air -> \t"
    ).upper()

    if len(escolha_usuario) > 1:
        print(
            "Escolha apenas a primeira letra!\n"
            "I -> para inserir\n"
            "A -> para apagar\n"
            "L -> para listar\n"
            "S -> para sair\n"
        )
        continue

    if escolha_usuario in opcoes_validas:
        os.system("clear")
        if escolha_usuario == "I":
            nova_insercao = input("Digite o produto: ")
            try:
                lista_de_compras.append(nova_insercao)
                if nova_insercao in lista_de_compras:
                    print("Produto adicionado!\n")
                else:
                    print("Algo deu errado. Tente novamente.\n")
            except:
                print("Problema no servidor. Tente novamente mais tarde!\n")
        elif escolha_usuario == "A":
            if len(lista_de_compras) == 0:
                print("A lista esta vazia!\n")
            else:
                for indice, produto in enumerate(lista_de_compras):
                    print(indice, produto)
                nova_exclusao = input("\nDigite o indice do produto a ser deletado: ")

                try:
                    nova_exclusao_indice = int(nova_exclusao)
                    del lista_de_compras[nova_exclusao_indice]
                    print("Produto deletado!\n")
                except IndexError:
                    print("Indice invalido (nao esta na lista)\n")
                except ValueError:
                    print("Digite apenas numeros inteiros!\n")
                except Exception:
                    print("Erro desconhecido!")

        elif escolha_usuario == "L":
            if len(lista_de_compras) == 0:
                print("A lista esta vazia!\n")
            else:
                for indice, produto in enumerate(lista_de_compras):
                    print(indice, produto)

        elif escolha_usuario == "S":
            break
