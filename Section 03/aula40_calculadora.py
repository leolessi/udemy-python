"""
Calculadora
"""

while True:
    sair = input("Deseja sair? [s]im ou [n]ao: ").lower().startswith("s")

    if sair:
        break
    else:
        try:
            primeiro_numero = input("Digite o primeiro numero: ")
            segundo_numero = input("Digite o segundo numero: ")
            operador_conta = input("Digite o operador da conta | + | - | / | * |: ")
            primeiro_numero_flt = float(primeiro_numero)
            segundo_numero_flt = float(segundo_numero)
            if operador_conta == "+":
                resultado = f"{primeiro_numero_flt} + {segundo_numero_flt} = {primeiro_numero_flt + segundo_numero_flt}"
            elif operador_conta == "-":
                resultado = f"{primeiro_numero_flt} - {segundo_numero_flt} = {primeiro_numero_flt - segundo_numero_flt}"
            elif operador_conta == "/":
                resultado = f"{primeiro_numero_flt} / {segundo_numero_flt} = {primeiro_numero_flt / segundo_numero_flt}"
            elif operador_conta == "*":
                resultado = f"{primeiro_numero_flt} * {segundo_numero_flt} = {primeiro_numero_flt * segundo_numero_flt}"
            else:
                resultado = "Digite um operador valido! +, -, / ou *"
        except:
            resultado = "Voce nao digitou um numero"

    print(resultado)
