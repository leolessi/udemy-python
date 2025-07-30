condicao = False

while not condicao:
    senha = input("Qual a senha para sair? ")

    if senha != "33":
        print(f"Senha invalida. Tente novamente.")
    else:
        condicao
        break

print("Senha correta. Fim do programa.")
