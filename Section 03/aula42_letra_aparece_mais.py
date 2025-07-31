# frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.".lower()

# Conta a frequência de cada letra, ignorando maiúsculas/minúsculas e desconsiderando espaços
# frase_lower = frase.lower()
# letra_mais = ""
# maior_qtd = 0
# for letra in frase_lower:
#     if letra.isalpha():
#         qtd = frase_lower.count(letra)
#         if qtd > maior_qtd:
#             maior_qtd = qtd
#             letra_mais = letra
# print(f'A letra que mais apareceu foi "{letra_mais}" ({maior_qtd}x)')
#
#
# -------------------------------------------------------------------------------
#
#
# frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.".lower()
#
# i = 0
# letras_mais_frequentes = []
# contagem_letras_mais_frequentes = 0

# while i < len(frase):
#     letra_atual = frase[i]
#     i += 1

#     if letra_atual == " ":
#         continue

#     qtd_letra_apareceu = frase.count(letra_atual)

#     if qtd_letra_apareceu > contagem_letras_mais_frequentes:
#         contagem_letras_mais_frequentes = qtd_letra_apareceu
#         letras_mais_frequentes = [letra_atual]

#     if (
#         qtd_letra_apareceu == contagem_letras_mais_frequentes
#         and letra_atual not in letras_mais_frequentes
#     ):
#         letras_mais_frequentes.append(letra_atual)

# print(
#     f"Letra mais frequente: {letras_mais_frequentes}. Apareceu {contagem_letras_mais_frequentes} vezes."
# )
#
#
#
#
frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.".lower()

i = 0
letras_mais_frequentes = []
contagem_letras_mais_frequentes = 0

while i < len(frase):
    letra_atual = frase[i]
    i += 1

    if letra_atual == " ":
        continue

    qtd_letra_apareceu = frase.count(letra_atual)

    if (
        qtd_letra_apareceu == contagem_letras_mais_frequentes
        and letra_atual not in letras_mais_frequentes
    ):
        letras_mais_frequentes.append(letra_atual)

    if qtd_letra_apareceu > contagem_letras_mais_frequentes:
        contagem_letras_mais_frequentes = qtd_letra_apareceu
        letras_mais_frequentes = [letra_atual]

print(
    f"Letra mais frequente: {letras_mais_frequentes}. Apareceu {contagem_letras_mais_frequentes} vezes."
)
