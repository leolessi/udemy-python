senha_fornecida = input("Digite sua senha: ")
senha_correta = "123456"

if not senha_fornecida:
    print("Voce nao digitou nenhuma senha")
elif senha_fornecida != senha_correta:
    print("Voce digitou a senha errada")
else:
    print("Voce digitou a senha correta!")

print(not True)  # retorna False
print(not False)  # retorna True

print(not 0)  # retorna True
print(not 1)  # retorna False
