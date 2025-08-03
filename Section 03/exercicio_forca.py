"""
Exercicio FORCA
1 -> escolher uma palavra (segredo)
2 -> solicitar uma letra para o usuario (letra_solicitada)
    2.1 -> acumular uma tentativa
    2.2 -> validacao para aceitar apenas uma letra (if... continue)
3 -> se a letra_solicitada estiver no segredo (if letra_solicitada in segredo) salvar essa letra em uma string (letras_solicitadas_corretas)
    3.1 -> validacao para aceitar apenas letras novas que ainda nao estejam nessa string (if letra_solicitada in letras_soli... continue)
4 -> percorrer as letras do segredo (for letras in segredo)
5 -> caso as letras estejam na string letra_solicitadas_corretas, printar a letra. Caso contrario, printar '*'
"""

segredo = "tentativas".upper()
letras_solicitadas_corretas = ""
tentativas = 0

while True:
    letra_solicitada = input("Digite uma letra: ").upper()
    tentativas += 1

    if len(letra_solicitada) > 1:
        print("Escolha apenas uma letra!")
        continue

    if letra_solicitada in segredo:
        if letra_solicitada not in letras_solicitadas_corretas:
            letras_solicitadas_corretas += letra_solicitada
        else:
            continue

    nova_resposta = ""
    for letra in segredo:
        if letra in letras_solicitadas_corretas:
            nova_resposta += letra
        else:
            nova_resposta += "*"

    if nova_resposta != segredo:
        print(nova_resposta)
    else:
        break

print(f"Parabéns, você encontrou a palavra '{segredo}' em {tentativas} tentativas!")


# ------------------------------------------------------------------------


# - pegar a letra do usuário
# - verificar se foi apenas uma letra fornecida, caso SIM, continuar o programa. Caso não, retornar o programa para a pergunta
# - verificar se a letra fornecida pelo usuário está na palavra secreta. Caso esteja, salvar essa letra em uma nova string junto com as letras que estão no segredo (letras_contidas_no_segredo)
# - percorrer as letras do segredo (for letra_secreta in segredo). Se a letra secreta for igual a letra fornecida, printar a letra fornecida. Se não for, printar um asterisco
# - para printar tudo em uma linha, iterar o print acima em uma nova string (nova frase += letra fornecida / nova frase += "*"
# - para não ter que percorrer o loop inteiro, verificar se a letra fornecida já faz parte da string letras_contidas_no_segredo
# - calcular o numero de tentativas (talvez limitar)


# segredo = "segredo".upper()
# letras_contidas_no_segredo = ""
# tentativas = 0

# while True:
#     letra_fornecida = input("Digite a letra: ").upper()
#     tentativas += 1

#     if len(letra_fornecida) > 1:
#         print("Digite apenas uma letra!")
#         continue

#     if letra_fornecida in segredo:
#         if letra_fornecida in letras_contidas_no_segredo:
#             continue
#         else:
#             letras_contidas_no_segredo += letra_fornecida

#     nova_palavra = ""
#     for letra_secreta in segredo:
#         if letra_secreta in letras_contidas_no_segredo:
#             nova_palavra += letra_secreta
#         else:
#             nova_palavra += "*"

#     print(nova_palavra)
#     if nova_palavra == segredo:
#         break

# print(
#     f"Você adivinhou a palavra secreta '{segredo.upper()}' em {tentativas} tentativas."
# )
