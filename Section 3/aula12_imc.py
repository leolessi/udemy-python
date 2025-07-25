nome = "Leonardo Lessi"
altura = 1.70
peso = 120
imc = peso / (altura * 2)

# print(
#     f"{nome} tem {altura:.2f} de altura, \npesa {peso} quilos e seu IMC é \n{imc:.4f}"
# )

print("{} tem {:.2f} de altura".format(nome, altura))
print("Pesa {} quilos".format(peso))
print("Tem IMC = {:.4f}".format(imc))
