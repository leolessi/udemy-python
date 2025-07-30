# condicao = False

# while not condicao:
#     senha = input("Qual a senha para sair? ")

#     if senha != "33":
#         print(f"Senha invalida. Tente novamente.")
#     else:
#         condicao
#         break

# print("Senha correta. Fim do programa.")
#
#
#
#
#
# contador = 0

# while contador < 10:
#     print(f"Contagem: foi acessado {contador + 1} vezes.")
#     contador += 1

# print("Fim do programa!")


# o continue faz voltar para a cabeça do while mais proximo
contador = -1

while contador <= 100:
    contador += 1

    if contador == 6:
        print("Nao vou mostrar o 6")
        continue

    if 27 >= contador >= 10:
        print("Nao vou mostrar o ", contador)
        continue

    print(contador)

    if contador == 33:
        break
