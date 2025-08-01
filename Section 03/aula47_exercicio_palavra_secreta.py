"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

"""
Solução com lista
"""

# import os

# palavra_secreta = "segredo".upper()
# lista_palavra_secreta = list(palavra_secreta)

# palavra_ocultada = "*" * len(palavra_secreta)
# lista_palavra_ocultada = list(palavra_ocultada)

# tentativas = 0

# while lista_palavra_ocultada != lista_palavra_secreta:
#     letra_informada = input("\nInforme a letra: ").upper()
#     tentativas += 1

#     if len(letra_informada) > 1:
#         print("Informe apenas uma letra!")
#         continue

#     for letra in lista_palavra_secreta:
#         i = 0
#         if letra_informada not in lista_palavra_secreta:
#             print(f"{letra_informada} nao esta dentro da palavra secreta")
#             break
#         else:
#             print(f"{letra_informada} esta dentro da palavra secreta")

#             while i < len(palavra_secreta):
#                 letra_atual = palavra_secreta[i]

#                 if letra_atual == letra_informada:
#                     lista_palavra_ocultada[i] = letra_atual

#                 i += 1
#             print(lista_palavra_ocultada)
#             break

# os.system("clear")

# print(
#     f"Você adivinhou a palavra secreta '{palavra_secreta}' em {tentativas} tentativas."
# )

"""
Solução com strings
"""

import os

segredo = "Perfume".upper()
letras_acertadas = "".upper()
tentativas = 0

while True:
    # pega a letra para tentar descobrir
    letra_atual = input("Digite uma letra: ").upper()
    tentativas += 1

    # validação: se mais de uma letra fornecida
    if len(letra_atual) > 1:
        print("Digite apenas UMA letra!")
        continue

    # verificação: se a letra fornecida faz parte do segredo
    if letra_atual in segredo:
        # se a letra fornecida já fizer parte da string de letras_acertadas, volta para o inicio do loop para não ter que percorrer todo o caminho
        if letra_atual in letras_acertadas:
            print((nova_frase).upper())
            continue

        # caso a letra fornecida não faça parte da string de letras_acertadas, concatena com a letra fornecida
        letras_acertadas += letra_atual

    # nova string para mostrar o resultado
    nova_frase = ""

    # percorre as letras do segredo atraves da variavel letra_secreta
    for letra_secreta in segredo:
        # se alguma letra do segredo estiver na posição da string letras_acertadas, concatena essa letra na posição da nova_frase
        if letra_secreta in letras_acertadas:
            nova_frase += letra_secreta
        # caso a letras não esteja nessa posição, concatena um * na posição da nova_frase
        else:
            nova_frase += "*"

    if nova_frase == segredo:
        break

    print((nova_frase).upper())

os.system("clear")
print(f"Voce descobriu o segredo ({nova_frase}) em {tentativas} tentativas")
