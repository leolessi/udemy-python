"""
split e join com list e str
split - divide uma string
join - une uma string
"""

# .strip corta os espacos dos lados / rstrip os espacos da direita e lstrip os da esquerda

frase = "   Olha so,    que  coisa       interessante!          "
lista_palavras_cruas = frase.split()

lista_palavras_fixed = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras_fixed.append(lista_palavras_cruas[i].strip())

palavras_unidas = " ".join(lista_palavras_fixed)
lista_generica = [
    "Amanda",
    "Bruno",
    "Camila",
    "Deuterostomio",
    "Eduardo",
    "Felipe",
    "Gabriela",
    "Humberto",
]

lista_generica = " | ".join(lista_generica)
print(lista_generica)

# print("Lista palavras cruas: ", lista_palavras_cruas)
# print("Lista palavras fixed: ", lista_palavras_fixed)
# print(palavras_unidas)

# frase_unidas = " | ".join(
#     [
#         "A",
#         "B",
#         "C",
#         "D",
#         "E",
#         "F",
#         "G",
#         "H",
#     ]
# )

# print(frase_unidas)
