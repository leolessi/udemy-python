"""
Exercicio 1: receber um num inteiro e retornar par ou impar. Caso nao seja um inteiro, informe
"""

# numero_recebido = input("Digite um numero inteiro: ")

# resultado = "Erro. Digite um número válido."

# if "." in numero_recebido or "," in numero_recebido:
#     resultado
# else:
#     int_numero_recebido = int(numero_recebido)
#     try:
#         if int_numero_recebido % 2 == 0:
#             resultado = "Par"
#         else:
#             resultado = "Impar"
#     except:
#         resultado = "Algo deu errado."

# print(resultado)


# metodo 2
# numero_recebido = input("Digite um número inteiro: ")

# if numero_recebido.isdigit():
#     numero_recebido_int = int(numero_recebido)
#     par_impar = numero_recebido_int % 2 == 0
#     resultado = "ímpar"

#     if par_impar:
#         resultado = "par"

#     print(f"O numero {numero_recebido_int} é {resultado}")
# else:
#     print("Você não digitou um número válido!")

"""
Exercício 2: entrada com hora do usuário. Retorna: Bom dia (0-11), Boa tarde (12-17) ou Boa noite (18-23).
"""

# hora_entrada = input("Digite a hora: ")

# try:
#     hora_entrada_int = int(hora_entrada)
#     if 23 >= hora_entrada_int >= 0:
#         if hora_entrada_int < 12:
#             resultado = "Bom dia!"
#         elif hora_entrada_int < 18:
#             resultado = "Boa tarde!"
#         else:
#             resultado = "Boa noite!"
#     else:
#         resultado = "Digite uma hora válida!"
# except:
#     resultado = "Digite um número inteiro!"

# print(resultado)

"""
Exercicio 3: Primeiro pede o nome do usuário, caso 4- letras (Seu nome é curto). Caso 5-6 letras (Seu nome é normal). 7+ (Seu nome é muito grande.)
"""

# nome_entrada = input("Digite o seu nome: ")

# try:
#     nome_tamanho = len(nome_entrada)
#     if nome_tamanho < 5:
#         resultado = "Nome curto!"
#     elif nome_tamanho < 7:
#         resultado = "Nome medio!"
#     else:
#         resultado = "Nome grande!"
# except:
#     reultad0 = "Algo deu errado!"

# print(resultado)
