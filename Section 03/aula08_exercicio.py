nome = "Leonardo"
sobrenome = "Lessi"

idade = 27
maior_de_idade = idade >= 18
if maior_de_idade:
    maior_de_idade = "Verdadeiro"
else:
    maior_de_idade = "Falso"

nascimento = 2025 - idade

altura_metros = 1.70

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura em metros:", altura_metros)
