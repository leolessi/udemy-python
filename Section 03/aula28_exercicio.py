"""
Peça ao usuário para digitar seu nome:
Peça ao usuário para digitar sua idade:
Se nome e idade forem digitados, exiba:
    Seu nome é:
    Seu nome invertido é:
    Seu nome contém (ou não) espaços:
    Seu nome tem {n} letras
    A primeira letra do seu nome é:
    A última letra do seu nome é:
Se nada for digitado em nome ou idade, exiba:
    "Desculpe, você deixou campos vazios."
"""

nome_usuario = input("Insira seu nome: ")
idade_str = input("Insira sua idade: ")

nome_usuario_len = len(nome_usuario)

if " " in nome_usuario:
    contem_espaco = "Seu nome contém espaços."
else:
    contem_espaco = "Seu nome não contém espaços."

if nome_usuario and idade_str:
    print(f"Seu nome: {nome_usuario}.")
    print(f"Seu nome invertido: {nome_usuario[::-1]}")
    print(f"{contem_espaco}")
    print(f"Seu nome tem {nome_usuario_len} letras.")
    print(f"A primeira letra do seu nome: {nome_usuario[0]}.")
    print(f"A última letra do seu nome: {nome_usuario[-1]}.")
else:
    print("Desculpe, você deixou campos vazios.")
