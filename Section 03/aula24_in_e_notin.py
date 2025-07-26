nome = "Leonardo"
# print(nome[1])
contem_letra = "a"
contem_letras = "ard"

# if contem_letra in nome:
#     print(f"O nome {nome} contem a letra {contem_letra}.")
# else:
#     print(f"O nome {nome} nao contem a letra {contem_letra}.")

# if contem_letra not in nome:
#     print(f"O nome {nome} nao contem a letra {contem_letra}.")
# else:
#     print(f"O nome {nome} contem a letra {contem_letra}.")

if contem_letras in nome:
    print(f"O nome {nome} contem a sequencia {contem_letras}.")
else:
    print(f"O nome {nome} nao contem a sequencia {contem_letras}.")

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)

numero = 10

if numero > 1:
    if numero > 2:
        if numero > 3:
            print("Número maior que 3")
        else:
            print("Número menor que 3")
    else:
        print("Número menor que 2")
else:
    print("Número menor que 1")
