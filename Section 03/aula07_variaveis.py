# PEP8: inicie variáveis com letras minúsculas. Podem ser usados números e underline
# O sinal de igual (=) é usado para atribuição de valor, diferente do sinal ==, que é usado para comparar dois valores.
# Exemplo: nome_completo = Leonardo Lessi

# nome_completo = "Leonardo Lessi"
# print(nome_completo)

primeiro_nome = "Leonardo"
sobrenome = "Lessi"

# print(primeiro_nome, sobrenome)

nome_completo = primeiro_nome + " " + sobrenome

idade = 17.999

maior_de_idade = idade >= 18
if maior_de_idade:
    maior_de_idade = "Verdadeiro"
else:
    maior_de_idade = "Falso"

print(
    "Nome: %s \nIdade: %s \nMaior de idade: %s \n"
    % (nome_completo, idade, maior_de_idade)
)

print(
    "Nome: {} \nIdade: {} \nMaior de idade: {} \n".format(
        nome_completo, idade, maior_de_idade
    )
)

print(f"Nome: {nome_completo} \nIdade: {idade} \nMaior de idade: {maior_de_idade}")
