nome = "Leonardo"

i = 0
novo_nome = ""

while i < len(nome):
    novo_nome = novo_nome + f"*{nome[i]}"
    i += 1

print(novo_nome)
