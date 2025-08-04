# nome1, nome2, nome3 = ["Leonardo", "Maria", "Helena"]
# print(nome2)

# nome1, *resto = ["Leonardo", "Maria", "Helena"]
# print(nome1, resto)

# por convenção, utiliza-se o _ (underline) para declarar o restante da lista que não será usada
# nome1, *_ = ["Leonardo", "Maria", "Helena"]

# print(nome1, _)

# lista = ["Leonardo", "Maria", "Helena"]
# tamanho_lista = len(lista)
# print(f"Tamanho da lista = {tamanho_lista}")
# print(f"Range da lista = {range(tamanho_lista)}")

# for i in range(tamanho_lista):
#     print(lista[i])

lista = ["Leonardo", "Maria", "Helena"]
tamanho_da_lista = len(lista)
nome1, nome2, nome3 = ["Leonardo", "Maria", "Helena"]

for i in range(tamanho_da_lista):
    print(lista[i])
